import { Menu, Sparkles, UserCircle2, X } from "lucide-react";
import { AnimatePresence, motion } from "framer-motion";
import { useEffect, useState } from "react";

function ThemeToggle({ theme, onToggle }) {
  return (
    <button
      type="button"
      onClick={onToggle}
      className="glass-pill justify-center px-3 py-2 text-xs sm:text-sm"
      aria-label="Toggle dark mode"
    >
      <span className="h-2.5 w-2.5 rounded-full bg-brand-400 shadow-glow" />
      {theme === "dark" ? "Dark" : "Light"}
    </button>
  );
}

function Navbar({ links, theme, onToggleTheme }) {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 18);
    handleScroll();
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <header className="sticky top-0 z-50 px-4 pt-4 sm:px-6 lg:px-8">
      <motion.nav
        className={`mx-auto flex w-full max-w-7xl items-center justify-between rounded-full border px-4 py-3 transition-all sm:px-6 ${
          scrolled
            ? "border-white/20 bg-slate-950/70 shadow-panel backdrop-blur-2xl"
            : "border-white/30 bg-white/50 backdrop-blur-xl dark:border-white/10 dark:bg-white/6"
        }`}
        initial={{ y: -28, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
      >
        <a href="#home" className="flex items-center gap-3">
          <span className="flex h-11 w-11 items-center justify-center rounded-2xl bg-gradient-to-br from-brand-400 to-sky-400 text-sm font-bold text-slate-950 shadow-glow">
            IE
          </span>
          <div>
            <p className="text-sm font-semibold tracking-[0.22em] text-brand-600 dark:text-brand-300">
              IEIRAS
            </p>
            <p className="text-xs text-slate-500 dark:text-slate-400">AI Climate Intelligence</p>
          </div>
        </a>

        <div className="hidden items-center gap-8 lg:flex">
          {links.map((link) => (
            <a
              key={link.href}
              href={link.href}
              className="text-sm font-medium text-slate-700 transition hover:text-brand-700 dark:text-slate-200 dark:hover:text-brand-300"
            >
              {link.label}
            </a>
          ))}
        </div>

        <div className="hidden items-center gap-3 lg:flex">
          <ThemeToggle theme={theme} onToggle={onToggleTheme} />
          <button className="glass-pill px-3 py-2">
            <UserCircle2 className="h-4 w-4" />
            Maya Chen
          </button>
          <a
            href="#contact"
            className="inline-flex items-center gap-2 rounded-full bg-slate-950 px-4 py-2.5 text-sm font-semibold text-white shadow-panel transition hover:-translate-y-0.5 dark:bg-brand-400 dark:text-slate-950"
          >
            <Sparkles className="h-4 w-4" />
            Request Demo
          </a>
        </div>

        <div className="flex items-center gap-2 lg:hidden">
          <ThemeToggle theme={theme} onToggle={onToggleTheme} />
          <button
            type="button"
            className="glass-pill px-3 py-2"
            onClick={() => setOpen((state) => !state)}
            aria-label="Toggle menu"
          >
            {open ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>
      </motion.nav>

      <AnimatePresence>
        {open ? (
          <motion.div
            className="mx-auto mt-3 w-full max-w-7xl rounded-3xl border border-white/20 bg-slate-950/88 p-4 shadow-panel backdrop-blur-2xl lg:hidden"
            initial={{ opacity: 0, y: -18 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -12 }}
          >
            <div className="flex flex-col gap-3">
              {links.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="rounded-2xl px-4 py-3 text-sm font-medium text-slate-100 transition hover:bg-white/8"
                  onClick={() => setOpen(false)}
                >
                  {link.label}
                </a>
              ))}
              <a
                href="#contact"
                className="mt-2 rounded-2xl bg-brand-400 px-4 py-3 text-center text-sm font-semibold text-slate-950"
                onClick={() => setOpen(false)}
              >
                Request Demo
              </a>
            </div>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </header>
  );
}

export default Navbar;
