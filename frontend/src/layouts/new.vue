<template>
  <v-app>
    <Sidebar />
    <Navbar />
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { onMounted } from "vue";
import { useAuth } from "vue-auth3";
import { login } from "@/services/login";

const auth = useAuth();

onMounted(() => {
  console.log(`${auth.check()}`);
});
</script>
