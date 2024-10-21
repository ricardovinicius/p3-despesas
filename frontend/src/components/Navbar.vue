<script>
import { useUiStore } from "@/stores/ui";

export default {
  setup() {
    const uiStore = useUiStore();
    const isEntradaOpen = false;
    const test = () => {
      console.log("test");
    };

    return { uiStore, test, isEntradaOpen }; // Retorna para usar no template
  },
};
</script>

<template>
  <v-app-bar :elevation="1" class="px-4 position-fixed">
    <template v-slot:prepend>
      <v-app-bar-nav-icon
        @click.stop="uiStore.toggleDrawer"
      ></v-app-bar-nav-icon>
      <v-btn icon="mdi-plus">
        <v-icon />
        <v-menu activator="parent">
          <v-list>
            <v-list-item id="entrada" value="entrada">
              <FooDialog activator="#entrada" tipo="entrada"></FooDialog>
              <v-list-item-title>Entrada</v-list-item-title>
            </v-list-item>
            <v-list-item id="saida" value="saida">
              <FooDialog activator="#saida" tipo="saida"></FooDialog>
              <v-list-item-title>Saída</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
    <template v-slot:append>
      <v-avatar>
        <v-icon icon="mdi-account-circle"></v-icon>
      </v-avatar>
    </template>
    <Dialog :isOpen="isEntradaOpen"></Dialog>
  </v-app-bar>
</template>
