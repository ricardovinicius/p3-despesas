import { defineStore } from "pinia";
import { list_transactions } from "@/services/transaction";
import { create_new_transaction } from "@/services/transaction";

export const useTransactionStore = defineStore("transaction", () => {
    const items = ref([]);
    
    async function fetchItems(auth) {
        const res = await list_transactions(auth);
        console.log(res);

        res.forEach((e) => {
            console.log(e);
            if (!items.value.includes()) {
                items.value.push({
                    descrição: e.description,
                    valor: e.value,
                    data: e.date,
                    categoria: e.category,
                });
            }
            
        });
    }

    function addTransaction(auth, transaction, type) {
        const _type = type === "entrada" ? "income" : "expense"; 
        create_new_transaction(auth, transaction, _type);
        fetchItems(auth);
    }

    return { items, fetchItems, addTransaction };
})