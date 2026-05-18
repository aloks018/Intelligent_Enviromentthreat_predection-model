import { useEffect, useState } from "react";

function AnimatedCounter({ value, suffix = "" }) {
  const [displayValue, setDisplayValue] = useState(0);

  useEffect(() => {
    let start = 0;
    const duration = 1300;
    const stepTime = Math.max(18, Math.floor(duration / Math.max(value, 1)));

    const timer = window.setInterval(() => {
      start += Math.max(1, Math.ceil(value / 36));
      if (start >= value) {
        setDisplayValue(value);
        window.clearInterval(timer);
      } else {
        setDisplayValue(start);
      }
    }, stepTime);

    return () => window.clearInterval(timer);
  }, [value]);

  return (
    <>
      {displayValue.toLocaleString()}
      {suffix}
    </>
  );
}

export default AnimatedCounter;
