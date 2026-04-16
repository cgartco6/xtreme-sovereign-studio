// Inside your Dashboard Component
<div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">
  <div className="bg-slate-900 border border-slate-800 p-8 rounded-3xl">
    <h3 className="text-blue-500 font-bold mb-4">Payout Schedule</h3>
    <div className="flex justify-between items-center py-2">
       <span>FNB (30% Ops)</span>
       <span className="text-green-400 font-mono">R {(revenue * 0.3).toLocaleString()}</span>
    </div>
    <div className="flex justify-between items-center py-2">
       <span>African Bank (20% Reserve)</span>
       <span className="text-orange-400 font-mono">R {(revenue * 0.2).toLocaleString()}</span>
    </div>
    <div className="mt-4 text-xs text-slate-500">Next Payout: Friday at 12:00 PM SAST</div>
  </div>
  
  <div className="bg-slate-900 border border-slate-800 p-8 rounded-3xl">
    <h3 className="text-purple-500 font-bold mb-4">Marketing Velocity</h3>
    <p className="text-sm text-slate-400">Posts Today: 12 / 24</p>
    <p className="text-sm text-slate-400">Total Leads Generated: 482</p>
    <div className="w-full bg-slate-800 h-2 mt-4 rounded-full overflow-hidden">
      <div className="bg-purple-500 h-full w-[65%]"></div>
    </div>
  </div>
</div>
