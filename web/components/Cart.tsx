import { useState } from 'react';

export default function Cart() {
  const [items, setItems] = useState([
    { id: 1, name: 'High-Enterprise Branding Kit', price: 499, description: 'Full Identity, PDF Guide, and Strategy Doc' }
  ]);

  const total = items.reduce((acc, item) => acc + item.price, 0);

  return (
    <div className="bg-slate-900 p-8 rounded-2xl border border-slate-800">
      <h2 className="text-2xl font-bold mb-6">Your Order Summary</h2>
      {items.map(item => (
        <div key={item.id} className="flex justify-between border-b border-slate-800 py-4">
          <div>
            <p className="font-bold text-lg">{item.name}</p>
            <p className="text-sm text-slate-500">{item.description}</p>
          </div>
          <p className="font-mono text-blue-400">${item.price}</p>
        </div>
      ))}
      <div className="mt-8 flex justify-between items-center">
        <span className="text-xl">Total: ${total}</span>
        <button className="bg-blue-600 hover:bg-blue-500 px-8 py-3 rounded-full font-bold transition">
          Checkout with Stripe
        </button>
      </div>
    </div>
  );
}
