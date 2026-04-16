export default function UpgradeDashboard({ ledgerBalance, upgradeQueue }) {
  return (
    <div className="p-10 bg-slate-950 min-h-screen text-white">
      <h1 className="text-3xl font-black mb-4">SYSTEM EVOLUTION</h1>
      <p className="text-blue-400 font-mono text-xl mb-10">
        Upgrade Ledger: R {ledgerBalance.toLocaleString()} (50% Revenue)
      </p>

      {['CRITICAL', 'MAJOR', 'MINOR'].map((level) => (
        <div key={level} className="mb-8">
          <h2 className={`text-sm font-bold tracking-widest mb-4 ${
            level === 'CRITICAL' ? 'text-red-500' : level === 'MAJOR' ? 'text-orange-500' : 'text-slate-500'
          }`}>{level} UPGRADES</h2>
          
          <div className="space-y-4">
            {upgradeQueue[level].map((item) => (
              <div key={item.id} className="bg-slate-900 border border-slate-800 p-6 rounded-2xl flex justify-between items-center">
                <div>
                  <p className="font-bold">{item.task}</p>
                  <p className="text-slate-500 text-sm">Cost: R {item.cost.toLocaleString()}</p>
                </div>
                <button 
                  disabled={ledgerBalance < item.cost}
                  className={`px-6 py-2 rounded-full font-bold ${
                    ledgerBalance >= item.cost ? 'bg-green-600 hover:bg-green-500' : 'bg-slate-800 text-slate-600'
                  }`}
                >
                  Approve & Deploy
                </button>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}
