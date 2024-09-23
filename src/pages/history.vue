<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Histórico</p>
      </v-col>
    </v-row>
    <v-row>
      <v-data-table :items="items"></v-data-table>
    </v-row>
  </v-container>
</template>

<script setup>
const items = [
  {
    descrição: "Comprei uma camisa na Shopee",
    valor: "R$ 42,00",
    data: "20/09/2024",
    categoria: "Compras",
  },
  // ... more items
];
</script>

<route lang="yaml">
meta:
  layout: new
</route>
