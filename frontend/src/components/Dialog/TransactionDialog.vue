<template>
  <v-dialog :activator="activator" max-width="600">
    <template v-slot:default="{ isActive }">
      <v-card class="pa-2">
        <v-card-title>{{ title }}</v-card-title>
        <v-form>
          <v-container>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="transaction.description"
                  label="Descrição"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-text-field
                  v-model="transaction.value"
                  label="Valor"
                ></v-text-field>
              </v-col>
              <v-col>
                <v-date-input v-model="transaction.date"></v-date-input>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <v-select
                  v-model="transaction.category"
                  label="Categoria"
                  :items="categories"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-form>
        <template v-slot:actions>
          <v-btn
            color="green"
            text="Adicionar"
            @click="
              () => {
                handleSubmit();
                isActive.value = false;
              }
            "
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
import { useTransactionStore } from "@/stores/transaction";
import { income_categories, expense_categories } from "@/utils/categories";

const transactionStore = useTransactionStore();

export default {
  props: ["activator", "tipo"],
  computed: {
    title() {
      return this.tipo == "entrada" ? "Adicionar entrada" : "Adicionar saída";
    },
    categories() {
      if (this.tipo == "entrada") {
        return income_categories.map((category) => category.title);
      } else {
        return expense_categories.map((category) => category.title);
      }
    },
  },
  data() {
    return {
      transaction: {
        description: "",
        value: 0,
        date: null,
        category: "",
      },
    };
  },
  methods: {
    handleSubmit() {
      transactionStore.addTransaction(this.$auth, this.transaction, this.tipo);
    },
  },
};
</script>
