import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import path from "path";

export default defineConfig({
  build: {
    outDir: path.resolve(__dirname, "../backend/static/"),
    emptyOutDir: true,
  },
  base: "./",
  server: {
    // host: "0.0.0.0", // Listen on all network interfaces
    // port: 3000, // Specify a port (default is 3000)
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5000",
        changeOrigin: true,
        secure: false,
      },
    },
  },
  plugins: [svelte()],
});
