<template>
  <div>
    <h1 class="font-weight-bold text-3xl text-center">FinanSys</h1>

    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Conta</div>

      <v-text-field
        v-model="email"
        density="compact"
        placeholder="Endereço de email"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>

      <div
        class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
      >
        Senha

        <a
          class="text-caption text-decoration-none text-blue"
          href="#"
          rel="noopener noreferrer"
          target="_blank"
        >
          Esqueceu a senha?</a
        >
      </div>

      <v-text-field
        v-model="password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Digite sua senha"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
        @click="submitForm"
      >
        Entrar
      </v-btn>

      <v-card-text class="text-center">
        <a
          class="text-blue text-decoration-none"
          href="#"
          @click.prevent="goToSignup"
          rel="noopener noreferrer"
          target="_blank"
        >
          Cadastre-se agora <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { login } from "@/services/auth";
import { useToast } from "vue-toastification";

const toast = useToast();

export default {
  data() {
    return {
      email: "",
      password: "",
      visible: false,
    };
  },
  methods: {
    submitForm() {
      this.$auth
        .login({
          data: {
            email: this.email,
            password: this.password,
          },
          redirect: "/",
          staySignedIn: true,
          fetchUser: true,
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);

            toast.error("Email ou senha inválidos");
          } else if (error.request) {
            console.log(error.request);

            toast.error("Erro no servidor");
          } else {
            console.log("Error", error.message);

            toast.error("Erro no servidor");
          }
          console.log(error.config);
        });
    },
    goToSignup() {
      this.$router.push("/signup"); // Corrigido: rota e nome do método
    },
  },
  beforeCreate() {
    if (this.$auth.check()) {
      this.$router.push("/");
    }
  },
};
</script>
