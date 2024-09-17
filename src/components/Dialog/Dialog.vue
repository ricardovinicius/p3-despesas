<template>
  <v-dialog :activator="activator">
    <template v-slot:default="{ isActive }">
      <v-card
        prepend-icon="mdi-variable"
        text="When using a ref, the dialog will bind its listeners to the ref element. This works for any element and custom components."
        title="Ref Activator"
      >
        <template v-slot:actions>
          <v-btn
            class="ml-auto"
            text="Close"
            @click="isActive.value = false"
          ></v-btn>
        </template>
      </v-card>
    </template>
  </v-dialog>
</template>

<script>
export default {
  props: ["activator"],
};
</script>
