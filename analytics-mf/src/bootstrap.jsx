import React from "react";
import { createRoot } from "react-dom/client";
import AnalyticsDashboard from "./components/AnalyticsDashboard";

const mount = (el, { token, user_id } = {}) => {
  const root = createRoot(el);
  root.render(<AnalyticsDashboard token={token} user_id={user_id} />);
};

const rootElement = document.getElementById("root");
if (rootElement) {
  const userData = JSON.parse(localStorage.getItem("user") || "{}");
  mount(rootElement, {
    token: localStorage.getItem("token"),
    user_id: userData.id,
  });
}

export { mount };
export default AnalyticsDashboard;
