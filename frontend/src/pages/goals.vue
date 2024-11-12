<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Metas</p>
      </v-col>
    </v-row>
    <!-- Renderiza o cartão de total apenas quando totalCard está pronto -->
    <v-row v-if="totalCard">
      <GoalCard :model="totalCard" />
    </v-row>
    <v-row>
      <v-divider class="my-6"></v-divider>
    </v-row>
    <!-- Renderiza cartões de categoria apenas quando categoryCards está carregado -->
    <v-row v-if="categoryCards.length > 0" v-for="categoryCard in categoryCards" :key="categoryCard.name">
      <GoalCard :model="categoryCard" />
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import GoalCard from "@/components/Card/GoalCard.vue";

export default {
  components: { GoalCard },
  data: () => ({
    totalCard: null,
    categoryCards: [],
  }),

  async mounted() {
    try {
      const response = await axios.get("/transaction/summary");
      const data = response.data;

      // Configura o cartão do total
      this.totalCard = {
        name: "Total",
        icon: "mdi-wallet",
        spend: data.total,
        goal: 1000, // Meta total, ajuste conforme necessário
      };

      // Configura os cartões de cada categoria
      this.categoryCards = data.category_expenses.map((expense) => {
        const icon = this.getCategoryIcon(expense.category);
        return {
          name: expense.category,
          icon: icon,
          spend: expense.total,
          goal: 100, // Meta por categoria, ajuste conforme necessário
        };
      });
    } catch (error) {
      console.error("Erro ao buscar dados da API:", error);
    }
  },

  methods: {
    getCategoryIcon(category) {
      const icons = {
        "Alimentação": "mdi-food",
        "Transporte": "mdi-car",
        "Saúde": "mdi-hospital",
        "Educação": "mdi-school",
        "Moradia": "mdi-home",
        "Lazer": "mdi-puzzle",
        "Compras": "mdi-cart",
        "Assinaturas e Serviços": "mdi-subscription",
        "Contas e Utilidades": "mdi-lightbulb",
        "Outros": "mdi-dots-horizontal",
      };
      return icons[category] || "mdi-help-circle";  // ícone padrão
    },
  },
};
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
