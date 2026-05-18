import { ArrowRight, Play, ShieldCheck } from "lucide-react";
import { motion } from "framer-motion";

import AnimatedCounter from "./AnimatedCounter";

function HeroSection({ counters, statCards }) {
  return (
    <section id="home" className="section-shell relative pt-10 sm:pt-14 lg:pt-20">
      <div className="glass-panel relative overflow-hidden px-6 py-8 sm:px-8 sm:py-10 lg:px-12 lg:py-14">
        <div
          className="absolute inset-0 bg-cover bg-center opacity-20 dark:opacity-30"
          style={{
            backgroundImage:
              "url('https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=2200&q=90')"
          }}
        />
        <div className="grid-ambient absolute inset-0 opacity-60" />
        <div className="relative grid gap-10 lg:grid-cols-[1.1fr_0.9fr] lg:items-center">
          <div className="max-w-3xl">
            <div className="glass-pill mb-5">
              <ShieldCheck className="h-4 w-4 text-brand-500" />
              Trusted environmental intelligence for policy, operations, and resilience teams
            </div>
            <motion.h1
              className="max-w-3xl text-4xl font-semibold leading-tight text-slate-950 sm:text-5xl lg:text-6xl dark:text-white"
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              AI Environmental
              <span className="block bg-gradient-to-r from-brand-500 via-teal-500 to-sky-500 bg-clip-text text-transparent">
                Intelligence Platform
              </span>
            </motion.h1>
            <motion.p
              className="mt-5 max-w-2xl text-base leading-8 text-slate-600 sm:text-lg dark:text-slate-300"
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.65, delay: 0.1 }}
            >
              Predict AQI, monitor water systems, analyze rainfall patterns, and surface climate
              risk faster with one premium operational workspace built for 2026 environmental
              decision teams.
            </motion.p>
            <motion.div
              className="mt-8 flex flex-col gap-3 sm:flex-row"
              initial={{ opacity: 0, y: 24 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.7, delay: 0.2 }}
            >
              <a
                href="#platform"
                className="inline-flex items-center justify-center gap-2 rounded-full bg-slate-950 px-6 py-3.5 text-sm font-semibold text-white shadow-panel transition hover:-translate-y-0.5 dark:bg-brand-400 dark:text-slate-950"
              >
                Explore Platform
                <ArrowRight className="h-4 w-4" />
              </a>
              <a
                href="#analytics"
                className="inline-flex items-center justify-center gap-2 rounded-full border border-white/50 bg-white/70 px-6 py-3.5 text-sm font-semibold text-slate-800 backdrop-blur transition hover:-translate-y-0.5 dark:border-white/10 dark:bg-white/10 dark:text-slate-100"
              >
                <Play className="h-4 w-4" />
                View Live Metrics
              </a>
            </motion.div>

            <div className="mt-10 grid gap-4 sm:grid-cols-3">
              {counters.map((counter, index) => (
                <motion.div
                  key={counter.label}
                  className="rounded-3xl border border-white/40 bg-white/70 p-5 shadow-sm backdrop-blur dark:border-white/10 dark:bg-white/8"
                  initial={{ opacity: 0, y: 28 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.2 + index * 0.08 }}
                >
                  <div className="text-3xl font-semibold text-slate-950 dark:text-white">
                    <AnimatedCounter value={counter.value} suffix={counter.suffix} />
                  </div>
                  <div className="mt-2 text-sm text-slate-500 dark:text-slate-300">{counter.label}</div>
                </motion.div>
              ))}
            </div>
          </div>

          <div className="relative flex min-h-[420px] items-center justify-center">
            <motion.div
              className="absolute inset-y-6 right-4 hidden w-24 rounded-full bg-brand-300/20 blur-3xl lg:block"
              animate={{ opacity: [0.45, 0.8, 0.45] }}
              transition={{ repeat: Infinity, duration: 5, ease: "easeInOut" }}
            />
            <div className="relative w-full max-w-xl">
              <motion.div
                className="glass-panel animate-float p-5"
                initial={{ opacity: 0, scale: 0.95 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.7, delay: 0.15 }}
              >
                <div className="rounded-[28px] border border-white/50 bg-gradient-to-br from-slate-950 via-teal-950 to-sky-950 p-6 text-white shadow-panel">
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm uppercase tracking-[0.28em] text-brand-200/70">
                        Live command layer
                      </p>
                      <p className="mt-2 text-2xl font-semibold">National climate readiness</p>
                    </div>
                    <div className="h-14 w-14 rounded-2xl border border-white/10 bg-white/10" />
                  </div>
                  <div className="mt-8 grid gap-4 sm:grid-cols-3">
                    {statCards.map((item) => (
                      <div
                        key={item.label}
                        className="rounded-3xl border border-white/10 bg-white/6 p-4 backdrop-blur"
                      >
                        <p className="text-xs uppercase tracking-[0.24em] text-slate-300/70">
                          {item.label}
                        </p>
                        <p className="mt-3 text-2xl font-semibold">{item.value}</p>
                        <p className="mt-2 text-sm text-slate-300/80">{item.detail}</p>
                      </div>
                    ))}
                  </div>
                </div>
              </motion.div>

              <motion.div
                className="glass-panel absolute -left-4 bottom-4 max-w-[220px] p-4 sm:-left-8"
                initial={{ opacity: 0, x: -24 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.7, delay: 0.25 }}
              >
                <p className="text-xs uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">
                  Automated insight
                </p>
                <p className="mt-2 text-sm font-medium text-slate-800 dark:text-slate-100">
                  Rainfall surge risk is trending down in central sectors, while water stress
                  remains elevated across river clusters.
                </p>
              </motion.div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default HeroSection;
