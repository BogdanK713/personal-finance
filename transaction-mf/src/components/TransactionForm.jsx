import React, { useState } from "react";

export default function TransactionForm({ onSuccess, token, user_id }) {
  const [form, setForm] = useState({
    category: "",
    amount: "",
    type: "Expense",
    date: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const body = { ...form, user_id };

    await fetch("http://localhost:3000/api/transactions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(body),
    });

    setForm({ category: "", amount: "", type: "Expense", date: "" });
    onSuccess();
  };

  return (
    <form onSubmit={handleSubmit} className="bg-gradient-to-br from-white to-gray-100 p-6 rounded-lg shadow-md space-y-4 border">
      <h3 className="text-xl font-semibold text-gray-800">➕ Add Transaction</h3>
      <div className="grid sm:grid-cols-2 gap-4">
        <input
          name="category"
          value={form.category}
          onChange={handleChange}
          className="border rounded px-4 py-2"
          placeholder="Category"
          required
        />
        <input
          name="amount"
          type="number"
          value={form.amount}
          onChange={handleChange}
          className="border rounded px-4 py-2"
          placeholder="Amount"
          required
        />
        <select
          name="type"
          value={form.type}
          onChange={handleChange}
          className="border rounded px-4 py-2"
        >
          <option value="Income">Income</option>
          <option value="Expense">Expense</option>
        </select>
        <input
          name="date"
          type="date"
          value={form.date}
          onChange={handleChange}
          className="border rounded px-4 py-2"
          required
        />
      </div>
      <button
        type="submit"
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition"
      >
        Add Transaction
      </button>
    </form>
  );
}
