/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import pinia from '@/stores'
import router from '@/router'
import auth from '@/plugins/auth'

export function registerPlugins (app) {
  app
    .use(vuetify)
    .use(router)
    .use(auth)
    .use(pinia)
}
