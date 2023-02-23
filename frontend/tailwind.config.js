/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./front/templates/**/*.html",
    "./front/static/src/**/*.js",
  ],
  theme: {
    container: {
      center: true,
    },
    extend: {
      colors: {
        swoops: {
          blue1: "#3568bf",
        },
      },
    },
  },
  plugins: [],
}
