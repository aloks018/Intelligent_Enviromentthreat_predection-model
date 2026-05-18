import {
  Activity,
  BrainCircuit,
  CloudRain,
  Droplets,
  Gauge,
  Map,
  Orbit,
  Waves
} from "lucide-react";

export const navLinks = [
  { label: "Overview", href: "#overview" },
  { label: "Platform", href: "#platform" },
  { label: "Analytics", href: "#analytics" },
  { label: "Map", href: "#map" },
  { label: "Contact", href: "#contact" }
];

export const statCards = [
  { label: "AQI accuracy", value: "96.4%", detail: "Model confidence across 22 urban zones" },
  { label: "Sensor uptime", value: "99.2%", detail: "Streams synced every 14 seconds" },
  { label: "Forecast horizon", value: "120h", detail: "Short-term weather and rainfall nowcast" }
];

export const counters = [
  { label: "Protected districts", value: 48, suffix: "+" },
  { label: "Live sensor feeds", value: 1260, suffix: "" },
  { label: "Prediction calls today", value: 18400, suffix: "" }
];

export const dashboardCards = [
  {
    title: "AQI Prediction",
    description: "Forecast air quality with model-backed alerts, sensitive-group guidance, and regional anomaly detection.",
    icon: Gauge,
    accent: "from-emerald-400/30 to-teal-500/10"
  },
  {
    title: "Weather Forecast",
    description: "Track pressure, humidity, wind, and cloud movement with operational forecast widgets.",
    icon: CloudRain,
    accent: "from-cyan-400/30 to-sky-500/10"
  },
  {
    title: "Rainfall Analytics",
    description: "Review runoff risk, monsoon trend shifts, and regional precipitation variance in one feed.",
    icon: Activity,
    accent: "from-blue-400/30 to-indigo-500/10"
  },
  {
    title: "Water Pollution Monitoring",
    description: "Detect contamination drift in rivers with nitrate, pH, turbidity, and conductivity tracking.",
    icon: Droplets,
    accent: "from-teal-400/30 to-emerald-500/10"
  },
  {
    title: "Ocean and Ice Tracking",
    description: "Monitor coastal stress, warming patterns, and cryosphere melt signals affecting resilience planning.",
    icon: Waves,
    accent: "from-sky-400/30 to-cyan-500/10"
  },
  {
    title: "AI Insights",
    description: "Turn raw environmental data into plain-language recommendations with scenario-aware summaries.",
    icon: BrainCircuit,
    accent: "from-violet-400/25 to-sky-500/10"
  },
  {
    title: "Real-Time Sensors",
    description: "Fuse station feeds, edge devices, and field updates into one operational command layer.",
    icon: Orbit,
    accent: "from-emerald-400/25 to-lime-500/10"
  },
  {
    title: "Live Maps",
    description: "Pinpoint local risk with geospatial markers, heat signatures, and response overlays.",
    icon: Map,
    accent: "from-blue-400/25 to-teal-500/10"
  }
];

export const trendData = [
  { month: "Jan", aqi: 88, water: 62, risk: 45 },
  { month: "Feb", aqi: 82, water: 66, risk: 42 },
  { month: "Mar", aqi: 74, water: 69, risk: 38 },
  { month: "Apr", aqi: 70, water: 72, risk: 35 },
  { month: "May", aqi: 76, water: 75, risk: 40 },
  { month: "Jun", aqi: 68, water: 78, risk: 31 }
];

export const rainfallData = [
  { name: "Mon", mm: 18 },
  { name: "Tue", mm: 26 },
  { name: "Wed", mm: 21 },
  { name: "Thu", mm: 31 },
  { name: "Fri", mm: 29 },
  { name: "Sat", mm: 24 },
  { name: "Sun", mm: 17 }
];

export const sensorData = [
  { time: "08:00", value: 82 },
  { time: "10:00", value: 84 },
  { time: "12:00", value: 79 },
  { time: "14:00", value: 77 },
  { time: "16:00", value: 73 },
  { time: "18:00", value: 71 }
];

export const forecastWidgets = [
  { label: "AQI next 24h", value: "74", status: "Moderate" },
  { label: "Rain chance", value: "68%", status: "Elevated" },
  { label: "Water quality", value: "92", status: "Stable" }
];

export const progressRings = [
  { label: "Air Stability", value: 74, tone: "text-emerald-400" },
  { label: "River Health", value: 81, tone: "text-cyan-400" },
  { label: "Coastal Readiness", value: 63, tone: "text-sky-400" }
];
