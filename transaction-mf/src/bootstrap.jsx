import React from "react";
import { createRoot } from "react-dom/client";
import './index.css';
import App from "./components/App";

const mount = (el, { token, user_id } = {}) => {
  const root = createRoot(el);
  root.render(<App token={token} user_id={user_id} />);
};

// Always mount if in development and root exists
const rootElement = document.getElementById("root");
if (rootElement) {
  const userData = JSON.parse(localStorage.getItem("user") || "{}");
  mount(rootElement, {
    token: localStorage.getItem("token"),
    user_id: userData.id, // ✅ use actual user ID
  });
}

export { mount };
export default App;
