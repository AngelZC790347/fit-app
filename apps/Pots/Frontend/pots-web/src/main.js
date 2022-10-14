import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./assets/main.css";


const app = createApp(App,{dni:76608998});

app.use(router)
app.mount("#app");
