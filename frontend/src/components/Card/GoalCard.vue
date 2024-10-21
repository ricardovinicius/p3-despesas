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
          <p class="align-center" v-show="!cardEdit">
            <v-icon icon="mdi-bullseye-arrow"></v-icon>
            R$ {{ model.goal }}
          </p>
          <v-text-field
            label="Meta"
            prepend-icon="mdi-bullseye-arrow"
            density="compact"
            variant="outlined"
            v-show="cardEdit"
            v-model="model.goal"
          ></v-text-field>
        </v-col>
      </v-row>
    </v-card-text>
    <v-card-actions class="text-end">
      <v-spacer></v-spacer>
      <v-btn variant="text" @click="cardEdit = !cardEdit">
        {{ cardEdit ? "Salvar" : "Editar" }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
const model = defineModel();
const cardEdit = ref(false);
</script>
