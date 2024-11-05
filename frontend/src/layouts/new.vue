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

const auth = useAuth();

onMounted(async () => {
  //const res = await auth.fetch({
  //  url: `${import.meta.env.VITE_API_URL}/user/me`,
  //});

  const user = auth.user().name;

  console.log(user);
});
</script>
