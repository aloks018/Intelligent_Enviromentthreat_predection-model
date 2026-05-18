import {
  Area,
  AreaChart,
  Bar,
  BarChart,
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis
} from "recharts";
import { motion } from "framer-motion";
import { ArrowUpRight, MapPinned, Radar, SignalHigh, Sparkles } from "lucide-react";

function DashboardModule({ icon: Icon, title, description, accent }) {
  return (
    <div className="group relative overflow-hidden rounded-[28px] border border-white/40 bg-white/70 p-5 shadow-sm backdrop-blur transition duration-300 hover:-translate-y-1 hover:shadow-glow dark:border-white/10 dark:bg-white/8">
      <div className={`absolute inset-x-0 top-0 h-24 bg-gradient-to-br ${accent} blur-2xl`} />
      <div className="relative">
        <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-slate-950 text-white dark:bg-white dark:text-slate-950">
          <Icon className="h-5 w-5" />
        </div>
        <h3 className="mt-4 text-lg font-semibold text-slate-950 dark:text-white">{title}</h3>
        <p className="mt-2 text-sm leading-7 text-slate-600 dark:text-slate-300">{description}</p>
      </div>
    </div>
  );
}

function ProgressRing({ label, value, tone }) {
  const radius = 44;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (value / 100) * circumference;

  return (
    <div className="rounded-[28px] border border-white/40 bg-white/70 p-5 text-center shadow-sm backdrop-blur dark:border-white/10 dark:bg-white/8">
      <div className="relative mx-auto h-28 w-28">
        <svg className="h-28 w-28 -rotate-90" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r={radius} stroke="rgba(148,163,184,0.18)" strokeWidth="10" fill="none" />
          <circle
            cx="60"
            cy="60"
            r={radius}
            stroke="currentColor"
            strokeWidth="10"
            fill="none"
            strokeLinecap="round"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            className={tone}
          />
        </svg>
        <div className="absolute inset-0 flex items-center justify-center">
          <div>
            <div className="text-2xl font-semibold text-slate-950 dark:text-white">{value}%</div>
            <div className="text-xs uppercase tracking-[0.2em] text-slate-500 dark:text-slate-400">
              Active
            </div>
          </div>
        </div>
      </div>
      <div className="mt-4 text-sm font-medium text-slate-700 dark:text-slate-100">{label}</div>
    </div>
  );
}

function UnifiedDashboard({
  cards,
  trendData,
  rainfallData,
  sensorData,
  widgets,
  progressRings
}) {
  return (
    <section id="platform" className="section-shell pt-16 sm:pt-20">
      <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <div className="glass-pill">Single unified dashboard</div>
          <h2 className="mt-4 text-3xl font-semibold text-slate-950 sm:text-4xl dark:text-white">
            One premium operational view for the full environmental stack
          </h2>
          <p className="mt-4 max-w-3xl text-base leading-8 text-slate-600 dark:text-slate-300">
            No duplicate admin panels. No fragmented cards. Just one professional control surface
            for AQI, weather, rainfall, water health, ocean stress, AI insights, sensors, and maps.
          </p>
        </div>
        <a
          href="#contact"
          className="inline-flex items-center gap-2 rounded-full border border-white/40 bg-white/70 px-5 py-3 text-sm font-semibold text-slate-800 shadow-sm backdrop-blur transition hover:-translate-y-0.5 dark:border-white/10 dark:bg-white/8 dark:text-slate-100"
        >
          Talk to the platform team
          <ArrowUpRight className="h-4 w-4" />
        </a>
      </div>

      <motion.div
        className="mt-8 grid gap-6 xl:grid-cols-[1.2fr_0.8fr]"
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        transition={{ duration: 0.55 }}
      >
        <div className="glass-panel overflow-hidden p-5 sm:p-6">
          <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                AI analytics graph
              </p>
              <h3 className="mt-2 text-2xl font-semibold text-slate-950 dark:text-white">
                Environmental signal intelligence
              </h3>
            </div>
            <div className="glass-pill">
              <SignalHigh className="h-4 w-4 text-brand-500" />
              Live confidence 96.4%
            </div>
          </div>
          <div id="analytics" className="mt-6 h-[320px]">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={trendData}>
                <defs>
                  <linearGradient id="aqiFill" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="5%" stopColor="#14b8a6" stopOpacity={0.4} />
                    <stop offset="95%" stopColor="#14b8a6" stopOpacity={0} />
                  </linearGradient>
                  <linearGradient id="waterFill" x1="0" x2="0" y1="0" y2="1">
                    <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.3} />
                    <stop offset="95%" stopColor="#38bdf8" stopOpacity={0} />
                  </linearGradient>
                </defs>
                <CartesianGrid stroke="rgba(148,163,184,0.14)" vertical={false} />
                <XAxis dataKey="month" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip contentStyle={{}} wrapperClassName="chart-tooltip" />
                <Area type="monotone" dataKey="aqi" stroke="#2dd4bf" strokeWidth={3} fill="url(#aqiFill)" />
                <Area
                  type="monotone"
                  dataKey="water"
                  stroke="#38bdf8"
                  strokeWidth={3}
                  fill="url(#waterFill)"
                />
                <Line type="monotone" dataKey="risk" stroke="#0f766e" strokeWidth={2} dot={false} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="grid gap-6">
          <div className="glass-panel p-5 sm:p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                  Forecast widgets
                </p>
                <h3 className="mt-2 text-xl font-semibold text-slate-950 dark:text-white">
                  Operational snapshot
                </h3>
              </div>
              <Sparkles className="h-5 w-5 text-brand-500" />
            </div>
            <div className="mt-5 space-y-3">
              {widgets.map((widget) => (
                <div
                  key={widget.label}
                  className="rounded-3xl border border-white/40 bg-white/70 p-4 shadow-sm dark:border-white/10 dark:bg-white/8"
                >
                  <div className="flex items-center justify-between gap-4">
                    <div>
                      <p className="text-sm text-slate-500 dark:text-slate-400">{widget.label}</p>
                      <p className="mt-2 text-2xl font-semibold text-slate-950 dark:text-white">
                        {widget.value}
                      </p>
                    </div>
                    <span className="rounded-full bg-brand-100 px-3 py-1 text-xs font-semibold text-brand-800 dark:bg-brand-400/15 dark:text-brand-200">
                      {widget.status}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="glass-panel p-5 sm:p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                  Circular progress
                </p>
                <h3 className="mt-2 text-xl font-semibold text-slate-950 dark:text-white">
                  Readiness indicators
                </h3>
              </div>
              <Radar className="h-5 w-5 text-sky-500" />
            </div>
            <div className="mt-5 grid gap-4 sm:grid-cols-3 xl:grid-cols-1 2xl:grid-cols-3">
              {progressRings.map((item) => (
                <ProgressRing key={item.label} {...item} />
              ))}
            </div>
          </div>
        </div>
      </motion.div>

      <motion.div
        className="mt-6 grid gap-6 lg:grid-cols-[0.95fr_1.05fr]"
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        transition={{ duration: 0.55, delay: 0.1 }}
      >
        <div className="glass-panel p-5 sm:p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                Rainfall analytics
              </p>
              <h3 className="mt-2 text-xl font-semibold text-slate-950 dark:text-white">
                Seven-day precipitation outlook
              </h3>
            </div>
            <span className="glass-pill">Monsoon variance: 12%</span>
          </div>
          <div className="mt-6 h-[280px]">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={rainfallData}>
                <CartesianGrid stroke="rgba(148,163,184,0.14)" vertical={false} />
                <XAxis dataKey="name" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip wrapperClassName="chart-tooltip" />
                <Bar dataKey="mm" radius={[10, 10, 4, 4]} fill="#14b8a6" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="glass-panel p-5 sm:p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                Real-time sensor data
              </p>
              <h3 className="mt-2 text-xl font-semibold text-slate-950 dark:text-white">
                Edge stream stability
              </h3>
            </div>
            <span className="glass-pill">Refresh 14s</span>
          </div>
          <div className="mt-6 h-[280px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={sensorData}>
                <CartesianGrid stroke="rgba(148,163,184,0.14)" vertical={false} />
                <XAxis dataKey="time" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip wrapperClassName="chart-tooltip" />
                <Line
                  type="monotone"
                  dataKey="value"
                  stroke="#38bdf8"
                  strokeWidth={3}
                  dot={{ stroke: "#38bdf8", strokeWidth: 2, fill: "#ffffff", r: 4 }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </motion.div>

      <motion.div
        className="mt-6 grid gap-6 lg:grid-cols-[1.08fr_0.92fr]"
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        transition={{ duration: 0.55, delay: 0.18 }}
      >
        <div id="map" className="glass-panel overflow-hidden p-5 sm:p-6">
          <div className="flex items-center justify-between gap-4">
            <div>
              <p className="text-sm uppercase tracking-[0.24em] text-brand-600 dark:text-brand-300">
                Live map intelligence
              </p>
              <h3 className="mt-2 text-xl font-semibold text-slate-950 dark:text-white">
                Geospatial awareness panel
              </h3>
            </div>
            <MapPinned className="h-5 w-5 text-sky-500" />
          </div>
          <div className="mt-6 rounded-[32px] border border-white/40 bg-slate-950 p-4 shadow-panel dark:border-white/10">
            <div
              className="relative min-h-[300px] overflow-hidden rounded-[24px] border border-white/10 bg-cover bg-center"
              style={{
                backgroundImage:
                  "url('https://images.unsplash.com/photo-1524661135-423995f22d0b?auto=format&fit=crop&w=1800&q=90')"
              }}
            >
              <div className="absolute inset-0 bg-gradient-to-br from-slate-950/45 via-teal-950/30 to-sky-900/45" />
              <div className="absolute left-[22%] top-[26%] h-3.5 w-3.5 rounded-full bg-brand-300 shadow-[0_0_0_12px_rgba(45,212,191,0.18)]" />
              <div className="absolute left-[58%] top-[38%] h-3.5 w-3.5 rounded-full bg-sky-300 shadow-[0_0_0_12px_rgba(56,189,248,0.18)]" />
              <div className="absolute left-[70%] top-[58%] h-3.5 w-3.5 rounded-full bg-emerald-300 shadow-[0_0_0_12px_rgba(110,231,183,0.18)]" />
              <div className="absolute bottom-5 left-5 right-5 rounded-[24px] border border-white/10 bg-slate-950/65 p-4 text-white backdrop-blur">
                <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
                  <div>
                    <p className="text-xs uppercase tracking-[0.24em] text-slate-300/70">
                      Active geo signal
                    </p>
                    <p className="mt-2 text-lg font-semibold">Eastern river corridor anomaly watch</p>
                  </div>
                  <div className="grid grid-cols-3 gap-3 text-sm">
                    <div>
                      <div className="text-slate-400">AQI</div>
                      <div className="font-semibold">71</div>
                    </div>
                    <div>
                      <div className="text-slate-400">Water</div>
                      <div className="font-semibold">92</div>
                    </div>
                    <div>
                      <div className="text-slate-400">Rain</div>
                      <div className="font-semibold">28mm</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="grid gap-6 sm:grid-cols-2">
          {cards.map((card) => (
            <DashboardModule key={card.title} {...card} />
          ))}
        </div>
      </motion.div>
    </section>
  );
}

export default UnifiedDashboard;
