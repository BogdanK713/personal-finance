import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "userApp/AuthContext";

const styles = {
  header: {
    background: "#ffffff",
    borderBottom: "1px solid #ddd",
    padding: "12px 0",
    position: "sticky",
    top: 0,
    zIndex: 999,
  },
  container: {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "0 20px",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
  },
  title: {
    fontSize: "20px",
    fontWeight: "bold",
    color: "#333",
  },
  links: {
    display: "flex",
    alignItems: "center",
    gap: "16px",
  },
  link: {
    textDecoration: "none",
    color: "#007bff",
    fontWeight: 500,
  },
  linkHover: {
    textDecoration: "underline",
  },
  logoutBtn: {
    backgroundColor: "#ff4d4d",
    color: "#fff",
    border: "none",
    padding: "6px 12px",
    cursor: "pointer",
    borderRadius: "4px",
    fontWeight: 500,
  },
};

const Navigation = () => {
  const { token, logout } = useAuth();

  return (
    <header style={styles.header}>
      <div style={styles.container}>
        <div style={styles.title}>💰 Finance Tracker</div>
        <nav style={styles.links}>
          {!token ? (
            <>
              <Link to="/login" style={styles.link}>Login</Link>
              <Link to="/register" style={styles.link}>Register</Link>
            </>
          ) : (
            <>
              <Link to="/profile" style={styles.link}>👤 Profile</Link>
              <Link to="/users" style={styles.link}>👥 Users</Link>
              <Link to="/transactions" style={styles.link}>💳 Transactions</Link>
              <Link to="/analytics" style={styles.link}>📊 Analytics</Link>
              <button style={styles.logoutBtn} onClick={logout}>🔓 Logout</button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Navigation;
