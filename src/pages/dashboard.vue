<template>
  <v-container class="pa-8" fluid>
    <v-row align="center">
      <v-col cols="9">
        <p class="text-h4">Dashboard</p>
      </v-col>
      <v-col cols="3">
        <v-select
          label=""
          :items="['Atual', 'Janeiro', 'Fevereiro', 'Março', 'Abril', '...']"
          v-model="current_item"
          density="comfortable"
        ></v-select>
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
          <v-spacer></v-spacer>
          <v-card-text class="text-h6">R$ 4.200,00</v-card-text>
        </v-card>
      </v-col>
      <v-col>
        <v-card color="red" class="fill-height d-flex flex-column">
          <v-card-title>Saídas </v-card-title>
          <v-spacer></v-spacer>
          <v-card-text class="text-h6">R$ 4.200,00</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
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
