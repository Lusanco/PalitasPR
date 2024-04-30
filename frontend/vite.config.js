import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    proxy: {
      // Replace with your Flask app's port
      // "/api": "http://localhost:5000",
      "/api": "http://127.0.0.1:5000",
    },
  },
  plugins: [svelte()],
});
