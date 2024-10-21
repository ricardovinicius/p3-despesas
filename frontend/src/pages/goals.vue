<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Metas</p>
      </v-col>
    </v-row>
    <v-row>
      <GoalCard v-model="totalCard"></GoalCard>
    </v-row>
    <v-row>
      <v-divider class="my-6"></v-divider>
    </v-row>
    <v-row>
      <GoalCard v-model="foodCard"></GoalCard>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cardEdit: false,
    totalCard: {
      name: "Total",
      icon: "mdi-wallet",
      spend: 30,
      goal: 100,
    },
    foodCard: {
      name: "Comida",
      icon: "mdi-food",
      spend: 30,
      goal: 100,
    },
  }),
};
</script>

<route lang="yaml">
meta:
  layout: new
</route>
