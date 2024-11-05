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
      <v-data-table :items="filteredItems"></v-data-table>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, computed } from "vue";

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

const items = [
  {
    descrição: "Comprei uma camisa na Shopee",
    valor: "R$ 42,00",
    data: "09/20/2024",
    categoria: "Compras",
  },
  {
    descrição: "Assinei Netflix",
    valor: "R$ 29,90",
    data: "09/18/2024",
    categoria: "Entretenimento",
  },
  {
    descrição: "Paguei conta de luz",
    valor: "R$ 150,00",
    data: "09/15/2024",
    categoria: "Contas",
  },
  {
    descrição: "Almoço no restaurante",
    valor: "R$ 45,00",
    data: "09/14/2024",
    categoria: "Alimentação",
  },
  {
    descrição: "Compra de passagem de ônibus",
    valor: "R$ 75,00",
    data: "09/13/2024",
    categoria: "Transporte",
  },
  {
    descrição: "Supermercado",
    valor: "R$ 220,00",
    data: "09/12/2024",
    categoria: "Alimentação",
  },
  {
    descrição: "Renovação de domínio",
    valor: "R$ 30,00",
    data: "09/10/2024",
    categoria: "Serviços",
  },
  {
    descrição: "Pagamento do cartão de crédito",
    valor: "R$ 1.200,00",
    data: "09/09/2024",
    categoria: "Contas",
  },
  {
    descrição: "Manutenção no carro",
    valor: "R$ 450,00",
    data: "09/07/2024",
    categoria: "Transporte",
  },
  {
    descrição: "Compra de presentes",
    valor: "R$ 90,00",
    data: "09/05/2024",
    categoria: "Compras",
  },
];

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
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
