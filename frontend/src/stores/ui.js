import { defineStore } from "pinia";

export const useUiStore = defineStore("ui", {
  state: () => ({
    drawer: false,
    theme: localStorage.getItem("theme"),
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
    toggleTheme() {
      this.theme = this.theme == "dark" ? "light" : "dark";
      localStorage.setItem("theme", this.theme);
    },
  },
});
