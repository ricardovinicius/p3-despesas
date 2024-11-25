<template>
  <div ref="reportRef">
    <v-theme-provider theme="light">
      <v-container class="pa-8" fluid>
        <v-row>
          <v-col cols="9">
            <p class="text-h4">
              Relatório de {{ transactionStore.selectedMonth }}
            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-card class="fill-height">
              <v-card-title>Olá, {{ auth.user().name }}!</v-card-title>
              <v-spacer></v-spacer>
              <v-card-text class="mr-8 font-italic"
                >Este é seu relatório mensal referente ao mês de
                {{ transactionStore.selectedMonth }}</v-card-text
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
                      <v-icon
                        :icon="get_expense_category_icon(item.categoria)"
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
        </v-row>
        <v-spacer></v-spacer>
        <v-row>
          <v-col>
            <v-card class="fill-height">
              <v-card-title>Balanço mensal </v-card-title>
              <v-container style="height: 48dvh">
                <Line ref="chart" :options="chartOptions" :data="datasets" />
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
        <v-row>
          <v-col>
            <v-card class="fill-height">
              <v-card-title>Histórico de Transações</v-card-title>
              <v-data-table-virtual
                :items="transactionStore.get_selected_month_items"
              ></v-data-table-virtual>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-theme-provider>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useTransactionStore } from "@/stores/transaction";
import { useAuth } from "vue-auth3";
import { income_categories, expense_categories } from "@/utils/categories";

const transactionStore = useTransactionStore();
const auth = useAuth();

const chartRef = useTemplateRef("chart");

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
      borderColor: "rgba(75, 192, 192, 1)",
    },
  ],
}));

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
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

import { useVueToPrint } from "vue-to-print";
import { onUpdated } from "vue";

const reportRef = useTemplateRef("reportRef");

const { handlePrint } = useVueToPrint({
  content: reportRef,
  documentTitle: "relatorio",
  removeAfterPrint: true,
});

onMounted(async () => {
  await transactionStore.fetchItems(auth);
  adjustMonths();
  console.log(transactionStore.get_month_balance);
  handlePrint();
});
</script>
