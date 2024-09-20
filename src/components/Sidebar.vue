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
  <v-navigation-drawer
    class="position-fixed"
    :rail="uiStore.isDrawerOpen"
    permanent
    :elevation="1"
  >
    <v-list-item class="text-center" title="FinanSys" lines="two"></v-list-item>
    <v-divider></v-divider>
    <v-list>
      <v-list-item
        prepend-icon="mdi-view-dashboard"
        link
        to="/dashboard"
        title="Dashboard"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-history"
        link
        to="/history"
        title="Histórico"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-cog"
        link
        title="Configurações"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
