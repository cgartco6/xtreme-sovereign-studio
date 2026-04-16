import Link from 'next/link';

export default function Navbar() {
  return (
    <nav className="border-b border-slate-800 bg-slate-950/50 backdrop-blur-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
        <Link href="/" className="text-xl font-black tracking-tighter text-white">
          XTREME<span className="text-blue-600">SOVEREIGN</span>
        </Link>
        <div className="space-x-8 text-sm font-medium text-slate-400">
          <Link href="/products" className="hover:text-white transition">Products</Link>
          <Link href="/about" className="hover:text-white transition">About</Link>
          <Link href="/contact" className="hover:text-white transition">Contact</Link>
          <Link href="/cart-summary" className="bg-slate-800 text-white px-4 py-2 rounded-full border border-slate-700">
            Cart (1)
          </Link>
        </div>
      </div>
    </nav>
  );
}
