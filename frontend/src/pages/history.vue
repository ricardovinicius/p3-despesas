<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="6">
        <p class="text-h4">Histórico</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6">
        <!-- Lupa para busca -->
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Buscar"
          solo
        ></v-text-field>
      </v-col>
      <v-col cols="3">
        <!-- Filtro por categoria -->
        <v-select
          v-model="selectedCategory"
          :items="categories"
          label="Filtrar por categoria"
          solo
          clearable
        ></v-select>
      </v-col>
      <v-col cols="3">
        <v-date-input
          v-model="date"
          multiple="range"
          prepend-icon=""
          prepend-inner-icon="$calendar"
        ></v-date-input>
      </v-col>
    </v-row>
    <v-row>
      <!-- Tabela com filtro de busca e categoria -->
      <v-data-table-virtual :items="filteredItems"></v-data-table-virtual>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { list_transactions } from "@/services/transaction";
import { useAuth } from "vue-auth3";
import { useTransactionStore } from "@/stores/transaction";

const auth = useAuth();

const search = ref("");
const selectedCategory = ref(null);
const date = ref();
const categories = [
  "Compras",
  "Entretenimento",
  "Contas",
  "Alimentação",
  "Transporte",
  "Serviços",
];
const transactionStore = useTransactionStore();

const items = reactive(transactionStore.items);

// Computed para filtrar os itens com base no texto da busca e na categoria selecionada
const filteredItems = computed(() => {
  let filtered = items;

  // Filtrar por categoria
  if (selectedCategory.value) {
    filtered = filtered.filter(
      (item) => item.categoria === selectedCategory.value
    );
  }

  // Filtrar por busca de texto
  if (search.value) {
    filtered = filtered.filter((item) =>
      Object.values(item).some((val) =>
        String(val).toLowerCase().includes(search.value.toLowerCase())
      )
    );
  }

  if (date.value && date.value.length > 0) {
    filtered = filtered.filter((item) => {
      return date.value.some((val) => {
        // Converte ambos item.data e val para objetos Date e compara seus timestamps
        const itemDate = new Date(item.data).setHours(0, 0, 0, 0); // Normaliza a hora
        const filterDate = new Date(val).setHours(0, 0, 0, 0); // Normaliza a hora
        return itemDate === filterDate;
      });
    });
  }

  return filtered;
});

onMounted(async () => {
  transactionStore.fetchItems(auth);
});
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
