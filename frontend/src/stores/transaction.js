import { defineStore } from "pinia";
import { list_transactions } from "@/services/transaction";
import { create_new_transaction } from "@/services/transaction";
import { ref } from "vue";
import { expense_categories } from "@/utils/categories";

export const useTransactionStore = defineStore("transaction", () => {
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

  const items = ref([]);
  const currentMonth = months[new Date().getMonth()];
  const selectedMonth = ref(currentMonth);

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

  const get_current_balance = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] <= selected_month_int
      );
    });

    const sum = selected_month_items.reduce((c, a) => {
      if (a.tipo == "Entrada") {
        c += a.valor;
      }
      if (a.tipo == "Saída") {
        c -= a.valor;
      }
      return c;
    }, 0);
    console.log(sum);
    return sum;
  });

  const get_current_income = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    const sum = selected_month_items.reduce((c, a) => {
      if (a.tipo == "Entrada") {
        c += a.valor;
      }
      return c;
    }, 0);
    console.log(sum);
    return sum;
  });

  const get_current_expense = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    const sum = selected_month_items.reduce((c, a) => {
      if (a.tipo == "Saída") {
        c += a.valor;
      }
      return c;
    }, 0);
    console.log(sum);
    return sum;
  });

  const get_last_incomes = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    const last_incomes = selected_month_items
      .reverse()
      .filter((i) => i.tipo == "Entrada");

    return last_incomes.slice(0, 3);
  });

  const get_last_expenses = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    const last_expenses = selected_month_items
      .reverse()
      .filter((i) => i.tipo == "Saída");
    console.log(last_expenses);
    return last_expenses.slice(0, 3);
  });

  const get_month_balance = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();

    const initial_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] < selected_month_int
      );
    });

    const initial_total = initial_month_items.reduce((c, a) => {
      if (a.tipo == "Entrada") {
        c += a.valor;
      }
      if (a.tipo == "Saída") {
        c -= a.valor;
      }
      return c;
    }, 0);

    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    let balance_value = initial_total;

    const balance_per_day = selected_month_items.reduce((acc, i) => {
      const { data, tipo, valor } = i;

      if (!acc[data]) {
        acc[data] = balance_value;
      }

      if (tipo == "Entrada") {
        balance_value += valor;
        acc[data] = balance_value;
      } else {
        balance_value -= valor;
        acc[data] = balance_value;
      }

      return acc;
    }, {});

    console.log(balance_per_day);
    return balance_per_day;
  });

  const get_expense_per_category = computed(() => {
    const selected_month_int =
      months.findIndex((m) => m === selectedMonth.value) + 1;
    const current_year = new Date().getFullYear();
    const selected_month_items = items.value.filter((i) => {
      return (
        i.data.split("-")[0] == current_year &&
        i.data.split("-")[1] == selected_month_int
      );
    });

    const expense_per_category = {};

    expense_categories.forEach((category) => {
      expense_per_category[category.title] = selected_month_items
        .filter((a) => a.categoria === category.title)
        .reduce((acc, b) => {
          return (acc += b.valor);
        }, 0);
    });

    console.log(expense_per_category);
    return expense_per_category;
  });

  return {
    items,
    selectedMonth,
    fetchItems,
    addTransaction,
    get_current_balance,
    get_current_income,
    get_current_expense,
    get_last_incomes,
    get_last_expenses,
    get_month_balance,
    get_expense_per_category,
  };
});
