class GlobalTaxEngine:
    """Calculates VAT/GST for EU, India, UAE, and USA."""
    def calculate_tax(self, amount, country_code):
        rates = {"ZA": 0.15, "UK": 0.20, "USA": 0.00, "EU": 0.21} # Simplified
        tax_amount = amount * rates.get(country_code, 0.15)
        return tax_amount
      
