<template>
  <v-card class="w-100 pa-2 ma-2">
    <v-card-title>
      <v-icon class="mr-2" :icon="model.icon"></v-icon>
      <span>{{ model.name }}</span>
    </v-card-title>
    <v-spacer></v-spacer>
    <v-card-text>
      <v-row>
        <v-col
          ><p>Valor Gasto: R$ {{ model.spend }}</p></v-col
        >
        <v-col
          ><p class="text-end">
            Resta: R$ {{ model.goal - model.spend }}
          </p></v-col
        >
      </v-row>
      <v-row class="mt-0">
        <v-slider
          :thumb-size="0"
          :model-value="model.spend"
          :color="model.spend > model.goal ? 'red' : 'green'"
          readonly
          :max="model.goal"
        ></v-slider>
      </v-row>
      <v-row class="mt-0">
        <v-spacer></v-spacer>
        <v-col class="text-end" cols="2">
          <v-btn variant="text" @click="toggleEdit">
            {{ cardEdit ? "Salvar" : "Editar" }}
          </v-btn>
        </v-col>
      </v-row>
      <v-row v-if="cardEdit">
        <v-col>
          <v-text-field
            label="Meta"
            prepend-icon="mdi-bullseye-arrow"
            density="compact"
            variant="outlined"
            v-model="model.goal"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useAuth } from "vue-auth3";
import auth from "@/plugins/auth";

const props = defineProps({
  model: {
    type: Object,
    required: true,
  },
  token: {
    type: String,
    required: true,
  },
});

console.log("props.model:", props.model);

const emit = defineEmits(["update-goal"]);

const cardEdit = ref(false);
const loading = ref(false); // Estado de carregamento
const model = ref({ ...props.model });

const fetchGoal = async () => {
  try {
    const auth = useAuth();
    const response = await axios.get(
      `${import.meta.env.VITE_API_URL}/goal/${model.value.name}?user_id=${
        auth.user().id
      }`,
      {
        headers: {
          Authorization: `Bearer ${auth.token()}`,
        },
      }
    );

    model.value.goal = response.data.goal;
  } catch (error) {
    console.error("Erro ao buscar meta:", error);
  }
};

onMounted(() => {
  fetchGoal(); // Busca o valor inicial da meta ao montar o componente
});

const toggleEdit = async () => {
  if (!cardEdit.value) {
    // Entrando no modo de edição
    cardEdit.value = true;
    return;
  }
  // Salvando no banco de dados
  loading.value = true;
  try {
    await axios.put(
      `${import.meta.env.VITE_API_URL}/goal/${props.model.name}?user_id=${
        auth.user().id
      }`,
      {
        goal: model.value.goal,
      },
      {
        headers: {
          Authorization: `Bearer ${props.token}`,
        },
      }
    );

    // Emite o evento para notificar o componente pai
    emit("update-goal", { ...props.model });
  } catch (error) {
    console.error("Erro ao atualizar meta:", error);
  } finally {
    loading.value = false;
    cardEdit.value = false; // Sai do modo de edição
  }
};
</script>
