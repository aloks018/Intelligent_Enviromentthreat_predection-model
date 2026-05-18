/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#ecfff8",
          100: "#cbfff0",
          200: "#9efce0",
          300: "#6cf0ce",
          400: "#33ddb8",
          500: "#11b999",
          600: "#0c927b",
          700: "#0c7565",
          800: "#0f5a50",
          900: "#103f39"
        },
        ink: {
          950: "#051216"
        }
      },
      fontFamily: {
        sans: ["Inter", "system-ui", "sans-serif"]
      },
      boxShadow: {
        glow: "0 24px 60px rgba(17, 185, 153, 0.18)",
        panel: "0 20px 60px rgba(4, 23, 27, 0.22)"
      },
      backgroundImage: {
        "mesh-light":
          "radial-gradient(circle at top left, rgba(37, 211, 177, 0.24), transparent 28%), radial-gradient(circle at top right, rgba(56, 189, 248, 0.18), transparent 32%), linear-gradient(180deg, rgba(240,253,250,1) 0%, rgba(235,250,248,1) 54%, rgba(245,250,255,1) 100%)",
        "mesh-dark":
          "radial-gradient(circle at top left, rgba(30, 206, 162, 0.22), transparent 28%), radial-gradient(circle at top right, rgba(59, 130, 246, 0.18), transparent 30%), linear-gradient(180deg, rgba(4,18,22,1) 0%, rgba(5,26,32,1) 55%, rgba(6,18,31,1) 100%)"
      },
      keyframes: {
        float: {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%": { transform: "translateY(-12px)" }
        },
        pulseSoft: {
          "0%, 100%": { opacity: "0.72", transform: "scale(1)" },
          "50%": { opacity: "1", transform: "scale(1.03)" }
        }
      },
      animation: {
        float: "float 6s ease-in-out infinite",
        pulseSoft: "pulseSoft 4.5s ease-in-out infinite"
      }
    }
  },
  plugins: []
};
