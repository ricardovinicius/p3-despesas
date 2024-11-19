<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Configurações</p>
      </v-col>
    </v-row>
    <v-row class="mx-3 my-3" @click="uiStore.toggleTheme()">
      <v-btn>Alterar tema</v-btn>
    </v-row>
  </v-container>
</template>

<script setup>
import { useUiStore } from "@/stores/ui";

const uiStore = useUiStore();
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
