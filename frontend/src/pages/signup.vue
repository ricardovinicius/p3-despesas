<template>
  <div>
    <h1 class="font-weight-bold text-3xl text-center">
      Cadastro de Usuário - FinanSys
    </h1>

    <v-card
      class="mx-auto pa-12 pb-8"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">
        Informações Básicas
      </div>

      <!-- Nome Completo -->
      <v-text-field
        density="compact"
        placeholder="Nome completo"
        prepend-inner-icon="mdi-account"
        variant="outlined"
        v-model="fullName"
      ></v-text-field>

      <!-- Endereço de Email -->
      <v-text-field
        density="compact"
        placeholder="Endereço de email"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
        v-model="email"
      ></v-text-field>

      <!-- Senha -->
      <v-text-field
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Digite sua senha"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        v-model="password"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <!-- Botão de Cadastro -->
      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
        @click="submitForm"
      >
        Cadastrar
      </v-btn>

      <!-- Link para Login -->
      <v-card-text class="text-center">
        <a
          class="text-blue text-decoration-none"
          href="#"
          rel="noopener noreferrer"
          @click="goToLogin"
        >
          Já tem uma conta? Entrar <v-icon icon="mdi-chevron-right"></v-icon>
        </a>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { register } from "@/services/auth";
import { useToast } from "vue-toastification";

const toast = useToast();

export default {
  data() {
    return {
      fullName: "",
      email: "",
      password: "",
      visible: false,
    };
  },
  methods: {
    submitForm() {
      // Adicionar a lógica de envio de cadastro aqui
      console.log(
        "Cadastro enviado:",
        this.fullName,
        this.email,
        this.password
      );
      this.$auth
        .register({
          data: {
            name: this.fullName,
            email: this.email,
            password: this.password,
          },
          autoLogin: true,
          redirect: "/",
        })
        .catch((error) => {
          if (error.response) {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);

            toast.error(error.response.data.detail);
          } else if (error.request) {
            console.log(error.request);
          } else {
            console.log("Error", error.message);
          }
          console.log(error.config);
        })

    },
    goToLogin() {
      this.$router.push("/login"); // Redireciona para a página de login
    },
  },
};
</script>
