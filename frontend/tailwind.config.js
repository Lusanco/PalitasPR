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
        theme: {
          "primary": "#F1F5F9",
          "secondary": "#2F3037",
          "accent": "#166534",
          "neutral": "#C6CBD2",
          /* "accentHover": "#12542B", */
          "error": "#cc2936",
        },
      },
    ],
  },
};
