import React from "react";

const Navbar = () => {
  return (
    <div style={styles.nav}>
      🧠 AI News Personalizer
    </div>
  );
};

const styles = {
  nav: {
    background: "#000",
    color: "#fff",
    padding: "15px",
    textAlign: "center",
    fontSize: "18px",
    fontWeight: "bold",
  },
};

export default Navbar;