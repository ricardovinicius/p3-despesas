<template>
  <v-card class="w-100 pa-2 ma-2">
    <v-card-title>
      <v-icon class="mr-2" icon="mdi-wallet"></v-icon>
      <span>Total</span>
    </v-card-title>
    <v-spacer></v-spacer>
    <v-card-text>
      <v-row>
        <v-col><p>Valor Gasto: R$ 30.00</p></v-col>
        <v-col><p class="text-end">Resta: R$ 70.00</p></v-col>
      </v-row>
      <v-row class="mt-0">
        <v-slider :thumb-size="0" model-value="30" readonly></v-slider>
      </v-row>
      <v-row class="mt-0">
        <v-spacer></v-spacer>
        <v-col class="text-end" cols="2">
          <p class="align-center" v-show="!cardEdit">
            <v-icon icon="mdi-bullseye-arrow"></v-icon>
            R$ 100.00
          </p>
          <v-text-field
            label="Meta"
            prepend-icon="mdi-bullseye-arrow"
            density="compact"
            variant="outlined"
            v-show="cardEdit"
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

<script>
export default {
  data: () => ({
    cardEdit: false,
  }),
};
</script>
