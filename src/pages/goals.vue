<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Metas</p>
      </v-col>
    </v-row>
    <v-row>
      <GoalCard></GoalCard>
    </v-row>
    <v-row>
      <v-divider class="my-6"></v-divider>
    </v-row>
    <v-row>
      <GoalCard></GoalCard>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    cardEdit: false,
  }),
};
</script>

<route lang="yaml">
meta:
  layout: new
</route>
