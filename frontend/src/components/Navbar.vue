<script>
import { useUiStore } from "@/stores/ui";
import { useAuth, useUser } from "vue-auth3";

export default {
  setup() {
    const uiStore = useUiStore();
    const isEntradaOpen = false;
    const test = () => {
      console.log("test");
    };
    const user = useUser();
    const auth = useAuth();

    const logoutHandler = () => {
      auth.logout({ makeRequest: false, redirect: "/login" });
    };

    return { uiStore, test, isEntradaOpen, user, logoutHandler }; // Retorna para usar no template
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
      <v-menu min-width="200px" rounded>
        <template v-slot:activator="{ props }">
          <v-btn icon v-bind="props">
            <v-avatar color="blue">
              <v-icon icon="mdi-account-circle"></v-icon>
            </v-avatar>
          </v-btn>
        </template>
        <v-card>
          <v-card-text>
            <div class="mx-auto text-center">
              <v-avatar color="blue">
                <v-icon icon="mdi-account-circle"></v-icon>
              </v-avatar>
              <h3>{{ user.name }}</h3>
              <p class="text-caption mt-1">
                {{ user.email }}
              </p>
              <v-divider class="my-3"></v-divider>
              <v-btn variant="text" rounded> Edit Account </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn variant="text" rounded @click.stop="logoutHandler()">
                Disconnect
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-menu>
    </template>
    <Dialog :isOpen="isEntradaOpen"></Dialog>
  </v-app-bar>
</template>
