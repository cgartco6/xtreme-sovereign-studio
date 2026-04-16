class SARSTaxEngine:
    """Real-time SARS compliance and tax-free threshold tracking."""
    def __init__(self):
        self.tax_free_limit = 600000  # R600k (2026 Turnover Tax Threshold)
        self.vat_compulsory = 2300000 # R2.3m (2026 VAT Threshold)

    def check_compliance(self, current_annual_turnover):
        if current_annual_turnover < self.tax_free_limit:
            return "✅ STATUS: Tax-Free Zone. No payment required."
        
        elif self.tax_free_limit <= current_annual_turnover < self.vat_compulsory:
            return "⚠️ REMINDER: Apply for 'Turnover Tax'. You are now in the 1%-3% bracket."
            
        elif current_annual_turnover >= self.vat_compulsory:
            return "🚨 ACTION REQUIRED: Compulsory VAT Registration. Contact SARS immediately."
          
