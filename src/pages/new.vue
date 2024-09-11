<template>
  <Sidebar />
  <Navbar />
  <v-container class="pa-8">
    <v-row>
      <v-col>
        <p class="text-h4">Dashboard</p>
        <v-breadcrumbs :items="['Foo', 'Bar', 'Fizz']"></v-breadcrumbs>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Bem vindo, Ricardo </v-card-title>
        </v-card>
      </v-col>
      <v-col>
        <v-card>
          <v-card-title>Balanço atual: </v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card color="green">
          <v-card-title>Entradas </v-card-title>
        </v-card>
      </v-col>
      <v-col>
        <v-card color="red">
          <v-card-title>Saídas </v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Balanço mensal </v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
//
</script>

<route lang="yaml">
meta:
  layout: new
</route>
