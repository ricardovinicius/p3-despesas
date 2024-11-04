import { createAuth } from "vue-auth3"
import router from '@/router'

import driverAuthBasic from "vue-auth3/drivers/auth/basic.js"
import driverHttpAxios from "vue-auth3/drivers/http/axios.js"

const auth = createAuth({
  plugins: {
    router,
  },
  drivers: {
    auth: driverAuthBasic,
    http: driverHttpAxios,
  },
})

export default auth;