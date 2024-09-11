<script>
import { useUiStore } from "@/stores/ui";

export default {
  setup() {
    const uiStore = useUiStore();

    return { uiStore };
  },
};
</script>

<template>
  <v-navigation-drawer :rail="uiStore.isDrawerOpen">
    <v-list-item class="text-center" title="Logo" lines="two"></v-list-item>
    <v-divider></v-divider>
    <v-list-item
      prepend-icon="mdi-account-multiple"
      link
      title="Dashboard"
    ></v-list-item>
    <v-list-item link title="Histórico"></v-list-item>
    <v-list-item link title="Metas"></v-list-item>
    <v-list-item link title="Relatórios"></v-list-item>
    <v-list-item link title="Configurações"></v-list-item>
  </v-navigation-drawer>
</template>
