import { useEffect, useState } from "react";

const Header = () => {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date());
    }, 60000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div style={styles.container}>
      <h1>
        {currentTime.toLocaleTimeString("hu-HU", {
          hour: "2-digit",
          minute: "2-digit",
        })}
      </h1>
      <h2>
        {currentTime.toLocaleDateString("hu-HU", {
          year: "numeric",
          month: "2-digit",
          day: "2-digit",
          weekday: "long",
        })}
      </h2>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    color: "#fff",
  },
} as const;

export default Header;
