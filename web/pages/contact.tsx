export default function Contact() {
  return (
    <div className="py-20 max-w-2xl mx-auto px-6">
      <h1 className="text-4xl font-bold mb-6">Connect with Xtreme</h1>
      <p className="text-slate-400 mb-10">Direct access for high-enterprise inquiries.</p>
      <form className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-slate-500 mb-2">Name</label>
          <input type="text" className="w-full bg-slate-900 border border-slate-800 rounded-lg p-3 focus:border-blue-500 outline-none" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-500 mb-2">Email</label>
          <input type="email" className="w-full bg-slate-900 border border-slate-800 rounded-lg p-3 focus:border-blue-500 outline-none" />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-500 mb-2">Message</label>
          <textarea rows={4} className="w-full bg-slate-900 border border-slate-800 rounded-lg p-3 focus:border-blue-500 outline-none"></textarea>
        </div>
        <button className="w-full bg-blue-600 py-4 rounded-lg font-bold hover:bg-blue-700 transition">
          Send Intelligence
        </button>
      </form>
    </div>
  );
}
