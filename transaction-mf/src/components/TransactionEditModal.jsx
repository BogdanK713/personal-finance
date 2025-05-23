import React, { useState } from "react";

export default function TransactionEditModal({ transaction, token, onClose, onSuccess }) {
  const [form, setForm] = useState({ ...transaction });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleUpdate = async (e) => {
    e.preventDefault();
    await fetch(`http://localhost:3000/api/transactions/${form.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(form),
    });
    onSuccess();
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-xl p-6 w-full max-w-md">
        <h3 className="text-xl font-bold mb-4">✏️ Edit Transaction</h3>
        <form onSubmit={handleUpdate} className="space-y-4">
          <input
            name="category"
            value={form.category}
            onChange={handleChange}
            className="w-full border rounded px-4 py-2"
            placeholder="Category"
            required
          />
          <input
            name="amount"
            type="number"
            value={form.amount}
            onChange={handleChange}
            className="w-full border rounded px-4 py-2"
            placeholder="Amount"
            required
          />
          <select
            name="type"
            value={form.type}
            onChange={handleChange}
            className="w-full border rounded px-4 py-2"
          >
            <option value="Income">Income</option>
            <option value="Expense">Expense</option>
          </select>
          <input
            name="date"
            type="date"
            value={form.date}
            onChange={handleChange}
            className="w-full border rounded px-4 py-2"
            required
          />
          <div className="flex justify-end gap-3 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 border border-gray-300 rounded hover:bg-gray-100"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 bg-green-600 text-white rounded hover:bg-green-700"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
