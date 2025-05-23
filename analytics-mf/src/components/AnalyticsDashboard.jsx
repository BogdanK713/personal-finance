import React, { useEffect, useState } from "react";

const API_BASE = "http://localhost:5000/api/analytics";

export default function AnalyticsDashboard({ token, user_id }) {
  const [summary, setSummary] = useState(null);
  const [monthly, setMonthly] = useState([]);
  const [budget, setBudget] = useState(null);

  const fetchAnalytics = async () => {
    const headers = { Authorization: `Bearer ${token}` };

    const [summaryRes, monthlyRes, budgetRes] = await Promise.all([
      fetch(`${API_BASE}/summary?user_id=${user_id}`, { headers }),
      fetch(`${API_BASE}/monthly?user_id=${user_id}`, { headers }),
      fetch(`${API_BASE}/budget?user_id=${user_id}`, { headers }),
    ]);

    const summaryData = await summaryRes.json();
    const monthlyData = await monthlyRes.json();
    const budgetData = await budgetRes.json();

    console.log("Summary:", summaryData);
    console.log("Monthly:", monthlyData);
    console.log("Budget:", budgetData);

    setSummary(summaryData);
    setMonthly(monthlyData.data || []);
    setBudget(budgetData);
  };

  useEffect(() => {
    fetchAnalytics();
  }, []);

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-center text-gray-800 mb-6">
        📊 Analytics Dashboard
      </h2>

      {summary && (
        <div className="bg-white rounded-lg shadow-md p-6 mb-6 border border-gray-200">
          <h3 className="text-xl font-semibold text-gray-700 mb-2">📌 Summary</h3>
          <p className="text-lg text-gray-600">
            <span className="font-medium text-gray-800">Total Transactions:</span>{" "}
            {summary.total_transactions}
          </p>
        </div>
      )}

      {monthly.length > 0 && (
        <div className="bg-white rounded-lg shadow-md p-6 mb-6 border border-gray-200">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">📆 Monthly Breakdown</h3>
          <ul className="space-y-2">
            {monthly.map((m, i) => (
              <li key={i} className="flex justify-between items-center px-4 py-2 bg-gray-50 rounded-md border border-gray-100">
                <span className="text-gray-700 font-medium">{m.month}</span>
                <span className="text-green-600">💰 {m.total_income}</span>
                <span className="text-red-500">💸 {m.total_expense}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {budget && (
        <div className="bg-white rounded-lg shadow-md p-6 border border-gray-200">
          <h3 className="text-xl font-semibold text-gray-700 mb-4">💼 Budget Status</h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="text-center">
              <p className="text-gray-600">Budget</p>
              <p className="text-xl font-bold text-blue-500">{budget.budget}</p>
            </div>
            <div className="text-center">
              <p className="text-gray-600">Spent</p>
              <p className="text-xl font-bold text-orange-500">{budget.spent}</p>
            </div>
            <div className="text-center">
              <p className="text-gray-600">Status</p>
              <p
                className={`text-xl font-bold ${
                  budget.status === "Under Budget" ? "text-green-600" : "text-red-600"
                }`}
              >
                {budget.status}
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
