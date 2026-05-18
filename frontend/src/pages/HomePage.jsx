import { useEffect, useMemo, useState } from "react";

import Footer from "../components/Footer";
import HeroSection from "../components/HeroSection";
import Loader from "../components/Loader";
import Navbar from "../components/Navbar";
import UnifiedDashboard from "../components/UnifiedDashboard";
import {
  counters,
  dashboardCards,
  forecastWidgets,
  navLinks,
  progressRings,
  rainfallData,
  sensorData,
  statCards,
  trendData
} from "../data/dashboard";

function HomePage() {
  const [loading, setLoading] = useState(true);
  const [theme, setTheme] = useState(() => {
    if (typeof window === "undefined") {
      return "dark";
    }

    return window.localStorage.getItem("ieiras-theme") || "dark";
  });

  useEffect(() => {
    const timer = window.setTimeout(() => setLoading(false), 1100);
    return () => window.clearTimeout(timer);
  }, []);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", theme === "dark");
    window.localStorage.setItem("ieiras-theme", theme);
  }, [theme]);

  const memoizedCards = useMemo(() => dashboardCards, []);

  return (
    <>
      {loading ? <Loader /> : null}
      <main id="overview" className="relative overflow-hidden">
        <Navbar
          links={navLinks}
          theme={theme}
          onToggleTheme={() => setTheme((current) => (current === "dark" ? "light" : "dark"))}
        />
        <HeroSection counters={counters} statCards={statCards} />
        <UnifiedDashboard
          cards={memoizedCards}
          trendData={trendData}
          rainfallData={rainfallData}
          sensorData={sensorData}
          widgets={forecastWidgets}
          progressRings={progressRings}
        />
        <Footer />
      </main>
    </>
  );
}

export default HomePage;
