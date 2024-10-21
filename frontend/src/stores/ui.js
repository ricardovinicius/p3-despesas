import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", {
  state: () => ({
    drawer: false,
  }),
  getters: {
    isDrawerOpen(state) {
      return state.drawer;
    },
  },
  actions: {
    toggleDrawer() {
      this.drawer = !this.drawer;
    },
  },
});
