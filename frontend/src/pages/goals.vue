<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Metas</p>
      </v-col>
    </v-row>
    <v-row v-if="totalCard">
      <GoalCard :model="totalCard" />
    </v-row>
    <v-row>
      <v-divider class="my-6"></v-divider>
    </v-row>
    <v-row v-for="categoryCard in categoryCards" :key="categoryCard.name">
      <GoalCard :model="categoryCard" />
    </v-row>
  </v-container>
</template>

<script>
import { useAuth } from "vue-auth3";
import axios from "axios";
import GoalCard from "@/components/Card/GoalCard.vue";

export default {
  components: { GoalCard },
  data() {
    return {
      totalCard: null,
      categoryCards: [],
    };
  },

  async mounted() {
    try {
      const auth = useAuth(); // Pega a instância de autenticação
      const token = auth.token();
      const userId = auth.user().id;

      // Realiza a requisição para buscar o resumo das transações
      const response = await axios.get(
        `${import.meta.env.VITE_API_URL}/transaction/summary?user_id=${userId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const data = response.data;

      // Configura o cartão de total
      this.totalCard = {
        name: "Total",
        icon: "mdi-wallet",
        spend: data.total || 0,
        goal: 1000, // Meta total
      };

      // Configura os cartões de cada categoria
      this.categoryCards = Array.isArray(data.category_expenses)
        ? data.category_expenses.map((expense) => ({
            name: expense.category || "Desconhecido",
            icon: this.getCategoryIcon(expense.category),
            spend: expense.total || 0,
            goal: 100, // Meta por categoria
          }))
        : [];
    } catch (error) {
      // Trata o erro e exibe no console
      console.error("Erro ao buscar dados da API:", error);
    }
  },

  methods: {
    getCategoryIcon(category) {
      const icons = {
        Alimentação: "mdi-food",
        Transporte: "mdi-car",
        Saúde: "mdi-hospital",
        Educação: "mdi-school",
        Moradia: "mdi-home",
        Lazer: "mdi-puzzle",
        Compras: "mdi-cart",
        Outros: "mdi-dots-horizontal",
      };
      return icons[category] || "mdi-help-circle"; // ícone padrão
    },
  },
};
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
