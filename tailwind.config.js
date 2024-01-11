/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    '!./.venv',
    './**/*.py',
    "./.venv/Lib/site-packages/crispy_tailwind/**/*.{html,py}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

