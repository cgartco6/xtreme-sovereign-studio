export default function BronwynChat() {
  return (
    <div className="fixed bottom-6 right-6 w-80 bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl overflow-hidden">
      <div className="bg-blue-600 p-4 text-white font-bold flex items-center justify-between">
        <span>Chat with Bronwyn</span>
        <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
      </div>
      <div className="h-64 p-4 overflow-y-auto text-sm text-slate-300">
        {/* Messages would map here */}
        <p className="bg-slate-800 p-2 rounded-lg mb-2">
          Hi! I'm Bronwyn. Ready to launch your enterprise for R599?
        </p>
      </div>
      <div className="p-4 border-t border-slate-800">
        <input 
          type="text" 
          placeholder="Ask Bronwyn..." 
          className="w-full bg-slate-950 border border-slate-800 rounded-xl p-2 text-white outline-none focus:border-blue-500"
        />
      </div>
    </div>
  );
}
