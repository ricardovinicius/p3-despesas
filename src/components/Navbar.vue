<script>
import { useUiStore } from "@/stores/ui";

export default {
  setup() {
    // Acessa a store
    const uiStore = useUiStore();

    return { uiStore }; // Retorna para usar no template
  },
};
</script>

<template>
  <v-app-bar :elevation="2">
    <template v-slot:prepend>
      <v-app-bar-nav-icon
        @click.stop="uiStore.toggleDrawer()"
      ></v-app-bar-nav-icon>
    </template>

    <v-app-bar-title>Application Bar</v-app-bar-title>
  </v-app-bar>
</template>
