export default function OrderSummary({ orderData }) {
  return (
    <div className="min-h-screen bg-slate-950 p-10">
      <div className="max-w-2xl mx-auto bg-slate-900 border border-slate-800 p-8 rounded-3xl">
        <h1 className="text-3xl font-bold text-green-500 mb-6">Payment Successful</h1>
        <p className="text-slate-400 mb-8">Your digital assets have been generated and are ready for download.</p>
        
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-slate-800 rounded-lg">
            <span>Brand_Strategy_Guide.pdf</span>
            <a href="/api/download/pdf" className="text-blue-400 font-bold">Download</a>
          </div>
          <div className="flex items-center justify-between p-4 bg-slate-800 rounded-lg">
            <span>Corporate_Identity.docx</span>
            <a href="/api/download/doc" className="text-blue-400 font-bold">Download</a>
          </div>
          <div className="flex items-center justify-between p-4 bg-blue-900/30 border border-blue-500/50 rounded-lg">
            <span className="font-bold">Full_Xtreme_Package.zip</span>
            <a href="/api/download/zip" className="text-white font-extrabold underline">Download All</a>
          </div>
        </div>
      </div>
    </div>
  )
}
