import React, { useEffect, useState } from "react";
import TransactionForm from "./TransactionForm";
import TransactionEditModal from "./TransactionEditModal";
import '../index.css';

export default function TransactionList({ token, user_id }) {
  const [transactions, setTransactions] = useState([]);
  const [editing, setEditing] = useState(null);

  const fetchTransactions = async () => {
    const res = await fetch(`http://localhost:3000/api/transactions?user_id=${user_id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    const data = await res.json();
    setTransactions(data);
  };

  const deleteTransaction = async (id) => {
    await fetch(`http://localhost:3000/api/transactions/${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    });
    fetchTransactions();
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  return (
    <div>
      <TransactionForm onSuccess={fetchTransactions} token={token} user_id={user_id} />
      <div className="mt-10">
        {transactions.length === 0 ? (
          <p className="text-gray-500 italic">No transactions yet. Start by adding one above.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full text-sm text-left text-gray-700 border rounded-lg overflow-hidden">
              <thead className="bg-gray-100 text-gray-800 uppercase tracking-wide">
                <tr>
                  <th className="px-6 py-3">Category</th>
                  <th className="px-6 py-3">Amount</th>
                  <th className="px-6 py-3">Type</th>
                  <th className="px-6 py-3">Date</th>
                  <th className="px-6 py-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y">
                {transactions.map((txn) => (
                  <tr key={txn.id} className="hover:bg-gray-50 transition-all">
                    <td className="px-6 py-3">{txn.category}</td>
                    <td className="px-6 py-3">{txn.amount}</td>
                    <td className="px-6 py-3">{txn.type}</td>
                    <td className="px-6 py-3">{txn.date}</td>
                    <td className="px-6 py-3 text-right space-x-2">
                      <button
                        onClick={() => setEditing(txn)}
                        className="text-blue-600 hover:text-blue-800 font-medium"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => deleteTransaction(txn.id)}
                        className="text-red-600 hover:text-red-800 font-medium"
                      >
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
      {editing && (
        <TransactionEditModal
          transaction={editing}
          token={token}
          onClose={() => setEditing(null)}
          onSuccess={() => {
            setEditing(null);
            fetchTransactions();
          }}
        />
      )}
    </div>
  );
}
