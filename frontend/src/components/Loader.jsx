import { motion } from "framer-motion";

function Loader() {
  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-slate-950">
      <div className="relative flex h-28 w-28 items-center justify-center">
        <motion.div
          className="absolute inset-0 rounded-full border border-brand-300/30"
          animate={{ scale: [1, 1.25, 1], opacity: [0.45, 0.1, 0.45] }}
          transition={{ duration: 2.2, repeat: Infinity, ease: "easeInOut" }}
        />
        <motion.div
          className="absolute inset-4 rounded-full border border-cyan-300/40"
          animate={{ scale: [1, 0.82, 1], opacity: [0.8, 0.2, 0.8] }}
          transition={{ duration: 1.8, repeat: Infinity, ease: "easeInOut" }}
        />
        <motion.div
          className="rounded-2xl bg-gradient-to-br from-brand-300 to-sky-400 px-5 py-3 text-sm font-semibold text-slate-950 shadow-glow"
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
        >
          IEIRAS
        </motion.div>
      </div>
    </div>
  );
}

export default Loader;
