<template>
  <v-container ref="dashboardRef" class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Dashboard</p>
      </v-col>
      <v-col class="d-flex justify-end" cols="3">
        <v-select
          label=""
          :items="getMonths"
          v-model="transactionStore.selectedMonth"
          density="comfortable"
          class="mr-4"
        ></v-select>
        <v-btn id="list-export-activator" icon="mdi-chevron-down"></v-btn>
        <v-menu activator="#list-export-activator">
          <v-list>
            <v-list-item value="export">
              <v-btn @click="handlePrint">Exportar relatório</v-btn>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="fill-height">
          <v-card-title>Bem vindo, {{ auth.user().name }}!</v-card-title>
          <v-spacer></v-spacer>
          <v-card-text class="mr-8 font-italic"
            >“Muitas pessoas gastam dinheiro que não tem, para comprar coisas
            que não precisam, para impressionar pessoas que não gostam.” - Will
            Smith</v-card-text
          >
        </v-card>
      </v-col>
      <v-col>
        <v-card class="fill-height d-flex flex-column">
          <v-card-title>Valor total: </v-card-title>
          <v-spacer></v-spacer>
          <v-card-text class="text-h6"
            >R$ {{ transactionStore.get_current_balance }}</v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="green" class="fill-height d-flex flex-column">
          <v-card-title>Entradas </v-card-title>
          <v-card-text>
            <p class="text-h6 text-bold">
              R$ {{ transactionStore.get_current_income }}
            </p>
            <p class="mt-4 font-weight-bold mb-2">Últimas Entradas:</p>
            <v-card
              variant="tonal"
              class="my-2"
              v-for="item in transactionStore.get_last_incomes"
            >
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon
                    :icon="get_income_category_icon(item.categoria)"
                    class="mr-4"
                  ></v-icon>
                  <div>
                    <p>{{ item.descrição }}</p>
                    <p>R$ {{ item.valor }}</p>
                  </div>
                  <div class="ml-auto">
                    <p>{{ item.data }}</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card color="red" class="fill-height d-flex flex-column">
          <v-card-title>Saídas </v-card-title>
          <v-card-text>
            <p class="text-h6 text-bold">
              R$ {{ transactionStore.get_current_expense }}
            </p>
            <p class="mt-4 font-weight-bold mb-2">Últimas Saídas:</p>
            <v-card
              variant="tonal"
              class="my-2"
              v-for="item in transactionStore.get_last_expenses"
            >
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>{{ item.descrição }}</p>
                    <p>R$ {{ item.valor }}</p>
                  </div>
                  <div class="ml-auto">
                    <p>{{ item.data }}</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="fill-height">
          <v-card-title>Balanço mensal </v-card-title>
          <v-container style="height: 50dvh">
            <Line :options="chartOptions" :data="datasets" />
          </v-container>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="fill-height">
          <v-card-title>Gasto por categoria</v-card-title>
          <v-list class="mx-4">
            <v-list-item
              :title="categoria"
              :subtitle="'R$ ' + (valor | 0)"
              :prepend-icon="get_expense_category_icon(categoria)"
              class="mb-2"
              v-for="(
                valor, categoria
              ) in transactionStore.get_expense_per_category"
            ></v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useTransactionStore } from "@/stores/transaction";
import { useAuth } from "vue-auth3";
import { income_categories, expense_categories } from "@/utils/categories";
import { useVueToPrint } from "vue-to-print";

const dashboardRef = ref();

const { handlePrint } = useVueToPrint({
  content: dashboardRef,
  documentTitle: "AwesomeFileName",
  removeAfterPrint: true,
});

const transactionStore = useTransactionStore();
const auth = useAuth();

const get_income_category_icon = (categoria) => {
  let icon = "mdi-help-circle";
  const category = income_categories.find((i) => {
    return i.title === categoria;
  });

  console.log(category);

  if (category) icon = category.icon;
  return icon;
};

const get_expense_category_icon = (categoria) => {
  let icon = "mdi-help-circle";
  const category = expense_categories.find((i) => {
    return i.title === categoria;
  });

  console.log(category);

  if (category) icon = category.icon;
  return icon;
};

const months = [
  "Janeiro",
  "Fevereiro",
  "Março",
  "Abril",
  "Maio",
  "Junho",
  "Julho",
  "Agosto",
  "Setembro",
  "Outubro",
  "Novembro",
  "Dezembro",
];

const getMonths = ref([...months]);

const adjustMonths = () => {
  const currentMonth = new Date().getMonth();
  getMonths.value = months.slice(0, currentMonth + 1).reverse();
};

import { onBeforeMount } from "vue";
import { Line } from "vue-chartjs";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

const datasets = computed(() => ({
  datasets: [
    {
      label: "Balanço Mensal",
      data: transactionStore.get_month_balance,
    },
  ],
}));

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
});

onBeforeMount(() => {
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
  );
  console.log("linetest: onBeforeMount");
});

onMounted(async () => {
  await transactionStore.fetchItems(auth);
  adjustMonths();
  console.log(transactionStore.get_month_balance);
});
</script>

<route lang="yaml">
meta:
  layout: new
  auth: true
</route>
