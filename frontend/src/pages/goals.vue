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
import { useTransactionStore } from "@/stores/transaction";

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

      const transactionStore = useTransactionStore();
      transactionStore.selectedMonth = transactionStore.currentMonth;
      await transactionStore.fetchItems(auth);

      // const transactionSummary = transactionSummaryResponse.data;
      const orderedGoals = [];
      /*const orderedGoals = transactionStore.get_expense_per_category.map(
        (expense) => ({
          name: expense.category || "Desconhecido",
          icon: this.getCategoryIcon(expense.category),
          spend: expense.total || 0,
          goal: 0, // Placeholder até que as metas sejam carregadas
        })
      );*/

      for (let category in transactionStore.get_expense_per_category) {
        orderedGoals.push({
          name: category || "Desconhecido",
          icon: this.getCategoryIcon(category),
          spend: transactionStore.get_expense_per_category[category] || 0,
          goal: 0, // Placeholder até que as metas sejam carregadas
        });
      }

      this.totalCard = {
        name: "Total",
        icon: this.getCategoryIcon("Total"),
        spend: transactionStore.get_current_expense,
        goal: 0,
      };

      this.categoryCards = orderedGoals;
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
    }
  },
  methods: {
    getCategoryIcon(category) {
      const icons = {
        Total: "mdi-cash",
        Alimentação: "mdi-food",
        Transporte: "mdi-car",
        Saúde: "mdi-hospital",
        Educação: "mdi-school",
        Moradia: "mdi-home",
        Lazer: "mdi-puzzle",
        Compras: "mdi-cart",
        Outros: "mdi-dots-horizontal",
      };
      return icons[category] || "mdi-help-circle";
    },
  },
};
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
