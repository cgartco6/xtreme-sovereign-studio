export default function ClientPortal({ order }) {
  return (
    <div className="max-w-4xl mx-auto py-20 px-6">
      <div className="flex justify-between items-center mb-12">
        <h1 className="text-3xl font-bold">Project Dashboard</h1>
        <span className="bg-green-500/20 text-green-400 px-4 py-1 rounded-full text-sm">Active</span>
      </div>
      
      <div className="grid grid-cols-1 gap-4">
        <div className="high-enterprise-card flex justify-between items-center">
          <div>
            <p className="font-bold">Digital Brand Identity Package</p>
            <p className="text-sm text-slate-500">Includes PDF Guidelines, DOCX Voice, and ZIP Assets</p>
          </div>
          <button className="btn-sovereign text-sm">Download All</button>
        </div>
      </div>
    </div>
  )
}
