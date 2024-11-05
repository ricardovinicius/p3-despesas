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
});

export default auth;
