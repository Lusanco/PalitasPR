/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{svelte,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("daisyui")],
  daisyui: {
    themes: [
      {
        mytheme: {
          // day: "#F1F1F1", // Anti-Flash White
          // night: "#1f1f1f", // Eerie Black
          // base: "#F1F1F1",
          // primary: "#0F766E", // bg-teal-800
          // "primary-content": "#E6FFFA", // text-teal-100
          // secondary: "#2DD4BF", // bg-teal-400
          // "secondary-content": "#0F766E", // text-teal-800
          // accent: "#5EEAD4", // bg-teal-400
          // neutral: "#3D4451",
          // "base-100": "#FFFFFF",
          // info: "#3ABFF8",
          // success: "#36D399",
          // warning: "#FBBD23",
          // error: "#F87272",
        },
      },
    ],
  },
};
