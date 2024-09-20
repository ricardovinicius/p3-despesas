<template>
  <v-dialog :activator="activator" max-width="600">
    <template v-slot:default="{ isActive }">
      <v-card class="pa-2">
        <v-card-title>{{ title }}</v-card-title>
        <v-form>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field label="Descrição"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field label="Valor"></v-text-field>
              </v-col>
              <v-col>
                <v-date-input></v-date-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select
                  label="Categoria"
                  :items="[
                    'California',
                    'Colorado',
                    'Florida',
                    'Georgia',
                    'Texas',
                    'Wyoming',
                  ]"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
        <template v-slot:actions>
          <v-btn
            color="green"
            text="Adicionar"
            @click="isActive.value = false"
          ></v-btn>
          <v-btn
            class="ml-auto"
            text="Cancelar"
            @click="isActive.value = false"
          ></v-btn>
        </template>
      </v-card>
    </template>
  </v-dialog>
</template>

<script>
export default {
  props: ["activator", "tipo"],
  computed: {
    title() {
      return this.tipo == "entrada" ? "Adicionar entrada" : "Adicionar saída";
    },
  },
};
</script>
