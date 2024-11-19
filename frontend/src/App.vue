<template>
  <v-app>
    <v-main>
      <v-theme-provider :theme="uiStore.theme">
        <router-view />
      </v-theme-provider>
    </v-main>
  </v-app>
</template>

<script setup>
import { useUiStore } from "./stores/ui";

const uiStore = useUiStore();
</script>
