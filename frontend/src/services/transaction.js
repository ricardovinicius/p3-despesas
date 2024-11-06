import axios from "axios";

const instance = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/transaction`,
})

export function create_new_transaction(auth, transaction, type) {
    console.log(transaction)

    const data = {
        type: type,
        description: transaction.description,
        value: transaction.value,
        date: transaction.date,
        category: transaction.category,
        user_id: auth.user().id
    }
    instance.post("", {
        data: data,
        headers: {"Authorization": `Bearer ${auth.token()}`},
    })
}