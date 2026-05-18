import { Github, Globe2, Linkedin, Mail } from "lucide-react";

function Footer() {
  return (
    <footer id="contact" className="section-shell py-16">
      <div className="glass-panel overflow-hidden px-6 py-8 sm:px-8">
        <div className="grid gap-8 lg:grid-cols-[1.1fr_0.6fr_0.6fr_0.8fr]">
          <div>
            <div className="flex items-center gap-3">
              <span className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-brand-400 to-sky-400 text-sm font-bold text-slate-950 shadow-glow">
                IE
              </span>
              <div>
                <p className="text-sm font-semibold tracking-[0.22em] text-brand-600 dark:text-brand-300">
                  IEIRAS
                </p>
                <p className="text-sm text-slate-500 dark:text-slate-400">
                  Environmental intelligence for the next decade
                </p>
              </div>
            </div>
            <p className="mt-5 max-w-md text-sm leading-7 text-slate-600 dark:text-slate-300">
              Premium AI decision support for air quality, climate forecasting, water monitoring,
              and resilient infrastructure planning.
            </p>
          </div>

          <div>
            <h3 className="text-sm font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">
              Quick links
            </h3>
            <div className="mt-4 space-y-3 text-sm text-slate-600 dark:text-slate-300">
              <a className="block hover:text-brand-600 dark:hover:text-brand-300" href="#overview">
                Overview
              </a>
              <a className="block hover:text-brand-600 dark:hover:text-brand-300" href="#platform">
                Platform
              </a>
              <a className="block hover:text-brand-600 dark:hover:text-brand-300" href="#analytics">
                Analytics
              </a>
            </div>
          </div>

          <div>
            <h3 className="text-sm font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">
              Contact
            </h3>
            <div className="mt-4 space-y-3 text-sm text-slate-600 dark:text-slate-300">
              <p>hello@ieiras.ai</p>
              <p>Climate Command Center</p>
              <p>Global SaaS Delivery, 2026</p>
            </div>
          </div>

          <div>
            <h3 className="text-sm font-semibold uppercase tracking-[0.24em] text-slate-500 dark:text-slate-400">
              Follow
            </h3>
            <div className="mt-4 flex flex-wrap gap-3">
              {[Github, Linkedin, Globe2, Mail].map((Icon, index) => (
                <a
                  key={index}
                  href="/"
                  className="inline-flex h-11 w-11 items-center justify-center rounded-2xl border border-white/40 bg-white/70 text-slate-700 shadow-sm backdrop-blur transition hover:-translate-y-0.5 dark:border-white/10 dark:bg-white/8 dark:text-slate-100"
                >
                  <Icon className="h-4 w-4" />
                </a>
              ))}
            </div>
          </div>
        </div>

        <div className="mt-8 border-t border-white/20 pt-6 text-sm text-slate-500 dark:border-white/10 dark:text-slate-400">
          Copyright 2026 IEIRAS. Built for environmental intelligence, climate resilience, and
          decision-ready operations.
        </div>
      </div>
    </footer>
  );
}

export default Footer;
