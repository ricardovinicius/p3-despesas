import { defineStore } from "pinia";
import { list_transactions } from "@/services/transaction";
import { create_new_transaction } from "@/services/transaction";
import { ref } from "vue";

export const useTransactionStore = defineStore("transaction", () => {
  const items = ref([]);

  async function fetchItems(auth) {
    const res = await list_transactions(auth);
    const new_items = [];
    res.forEach((e) => {
      new_items.push({
        tipo: e.type === "income" ? "Entrada" : "Saída",
        descrição: e.description,
        valor: e.value,
        data: e.date,
        categoria: e.category,
      });
    });
    items.value = new_items;
  }

  async function addTransaction(auth, transaction, type) {
    const _type = type === "entrada" ? "income" : "expense";
    console.log(transaction);
    create_new_transaction(auth, transaction, _type);
    await fetchItems(auth);
  }

  return { items, fetchItems, addTransaction };
});
