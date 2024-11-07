import axios from "axios";

const instance = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/transaction`,
})

export function create_new_transaction(auth, transaction, type) {
    const date = `${transaction.date.getFullYear()}-${transaction.date.getMonth().toString().padStart(2, '0')}-${transaction.date.getDay().toString().padStart(2, '0')}`

    const data = {
        type: type,
        description: transaction.description,
        value: transaction.value,
        date: date,
        category: transaction.category,
        user_id: auth.user().id
    }

    console.log(data)

    instance.post("", data, {
        headers: {"Authorization": `Bearer ${auth.token()}`},
    }).catch((error) => {
        if (error.response) {
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
        } else if (error.request) {
          console.log(error.request);
        } else {
          console.log("Error", error.message);
        }
        console.log(error.config);
      });
}