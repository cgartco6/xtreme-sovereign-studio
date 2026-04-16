import Navbar from '../components/Navbar';

const products = [
  { id: 1, name: 'Sovereign Brand Kit', price: '$499', features: ['AI Logo Gen', 'Brand Voice PDF', 'Strategic Doc'] },
  { id: 2, name: 'Institutional Marketing Suite', price: '$899', features: ['Full Ad Copy', 'Market Analysis', 'PDF + ZIP'] },
  { id: 3, name: 'Custom Agency Infrastructure', price: '$1,999', features: ['Full Codebase', 'Cloud Setup', '24/7 Support'] },
];

export default function Products() {
  return (
    <div className="min-h-screen bg-slate-950">
      <Navbar />
      <div className="max-w-7xl mx-auto py-20 px-6">
        <h1 className="text-4xl font-extrabold mb-12">Digital Solutions</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {products.map((p) => (
            <div key={p.id} className="bg-slate-900 border border-slate-800 p-8 rounded-3xl hover:border-blue-500 transition">
              <h2 className="text-2xl font-bold mb-2">{p.name}</h2>
              <p className="text-3xl text-blue-400 font-mono mb-6">{p.price}</p>
              <ul className="text-slate-400 mb-8 space-y-2">
                {p.features.map(f => <li key={f}>• {f}</li>)}
              </ul>
              <button className="w-full bg-blue-600 py-3 rounded-xl font-bold hover:bg-blue-500 transition">
                Add to Cart
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
