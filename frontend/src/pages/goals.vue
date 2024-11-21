<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Metas</p>
      </v-col>
    </v-row>
    <v-row v-if="totalCard">
      <GoalCard :model="totalCard" :token="token" />
    </v-row>
    <v-row>
      <v-divider class="my-6"></v-divider>
    </v-row>
    <v-row v-for="categoryCard in categoryCards" :key="categoryCard.name">
      <GoalCard :model="categoryCard" :token="token" />
    </v-row>
  </v-container>
</template>

<script>
import { computed } from "vue";
import { useAuth } from "vue-auth3";
import axios from "axios";
import GoalCard from "@/components/Card/GoalCard.vue";

export default {
  components: { GoalCard },
  setup() {
    const auth = useAuth(); // Instância de autenticação
    const token = computed(() => auth.token()); // Computed para o token
    return { auth, token }; // Torne acessível no template
  },
  data() {
    return {
      totalCard: null,
      categoryCards: [],
    };
  },
  async mounted() {
    try {
      const auth = useAuth();
      const token = auth.token();
      const userId = auth.user().id;

      const transactionSummaryResponse = await axios.get(
        `${import.meta.env.VITE_API_URL}/transaction/summary?user_id=${userId}`,
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const transactionSummary = transactionSummaryResponse.data;
      const orderedGoals = transactionSummary.category_expenses.map((expense) => ({

        name: expense.category || "Desconhecido",
        icon: this.getCategoryIcon(expense.category),
        spend: expense.total || 0,
        goal: 0, // Placeholder até que as metas sejam carregadas
      }));

      this.categoryCards = orderedGoals;
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
    }
  },
  methods: {
    getCategoryIcon(category) {
      const icons = {
        Food: "mdi-food",
        Transport: "mdi-car",
        Health: "mdi-hospital",
        Education: "mdi-school",
        Housing: "mdi-home",
        Leisure: "mdi-puzzle",
        Shopping: "mdi-cart",
        Others: "mdi-dots-horizontal",
      };
      return icons[category] || "mdi-help-circle";
    },
  },
};
</script>
