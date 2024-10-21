<template>
  <v-container class="pa-8" fluid>
    <v-row>
      <v-col cols="9">
        <p class="text-h4">Dashboard</p>
      </v-col>
      <v-col class="d-flex justify-end" cols="3">
        <v-select
          label=""
          :items="['Atual', 'Janeiro', 'Fevereiro', 'Março', 'Abril', '...']"
          v-model="current_item"
          density="comfortable"
          class="mr-4"
        ></v-select>
        <v-btn id="list-export-activator" icon="mdi-chevron-down"></v-btn>
        <v-menu activator="#list-export-activator">
          <v-list>
            <v-list-item value="export">Exportar relatório</v-list-item>
          </v-list>
        </v-menu>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card class="fill-height">
          <v-card-title>Bem vindo, Ricardo!</v-card-title>
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
          <v-card-title>Balanço atual: </v-card-title>
          <v-spacer></v-spacer>
          <v-card-text class="text-h6">R$ 4.200,00</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="green" class="fill-height d-flex flex-column">
          <v-card-title>Entradas </v-card-title>
          <v-card-text>
            <p class="text-h6 text-bold">R$ 4.200,00</p>
            <p class="mt-4 font-weight-bold mb-2">Entradas Recentes:</p>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
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
            <p class="text-h6 text-bold">R$ 4.200,00</p>
            <p class="mt-4 font-weight-bold mb-2">Saídas Recentes:</p>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
            <v-card variant="tonal" class="my-2">
              <v-card-text class="pa-2">
                <div class="d-flex align-center">
                  <v-icon icon="mdi-food" class="mr-4"></v-icon>
                  <div>
                    <p>Teste</p>
                    <p>R$ 4200.00</p>
                  </div>
                  <div class="ml-auto">
                    <p>20/09/2024</p>
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
          <v-container>
            <v-sparkline
              :auto-line-width="autoLineWidth"
              :fill="fill"
              :gradient="gradient"
              :gradient-direction="gradientDirection"
              :line-width="width"
              :model-value="value"
              :padding="padding"
              :smooth="radius || false"
              :stroke-linecap="lineCap"
              :type="type"
              auto-draw
            ></v-sparkline>
          </v-container>
        </v-card>
      </v-col>
      <v-col>
        <v-card class="fill-height">
          <v-card-title>Gasto por categoria</v-card-title>
          <v-list class="mx-4">
            <v-list-item
              title="Alimentação"
              subtitle="R$ 4200.00"
              prepend-icon="mdi-food"
            ></v-list-item>
            <v-list-item
              title="Alimentação"
              subtitle="R$ 4200.00"
              prepend-icon="mdi-food"
            ></v-list-item>
            <v-list-item
              title="Alimentação"
              subtitle="R$ 4200.00"
              prepend-icon="mdi-food"
            ></v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
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
import { Line } from "vue-chartjs";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"],
];

export default {
  components: {
    Line,
  },
  data: () => ({
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: "round",
    gradient: gradients[5],
    value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
    gradientDirection: "top",
    gradients,
    fill: false,
    type: "trend",
    autoLineWidth: false,
    current_item: "Atual",
  }),
};
</script>

<route lang="yaml">
meta:
  layout: new
</route>
