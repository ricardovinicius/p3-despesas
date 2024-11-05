import { createAuth } from "vue-auth3";
import router from "@/router";

import driverAuthBearerToken from "vue-auth3/drivers/auth/bearer-token.js";
import driverHttpAxios from "vue-auth3/drivers/http/axios.js";

const auth = createAuth({
  plugins: {
    router,
  },
  drivers: {
    auth: driverAuthBearerToken,
    http: driverHttpAxios,
  },
  registerData: {
    url: `${import.meta.env.VITE_API_URL}/user`
  },
  loginData: {
    url: `${import.meta.env.VITE_API_URL}/user/login`,
  },
  fetchData: {
    url: `${import.meta.env.VITE_API_URL}/user/me`,
  }
});

export default auth;
