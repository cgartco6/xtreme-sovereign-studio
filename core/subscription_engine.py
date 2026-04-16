class SubscriptionEngine:
    """Manages recurring ZAR billing to push past the R1M/month mark."""
    def __init__(self):
        self.tiers = {
            "BASIC_MAINTENANCE": 299, # Hosting + Security
            "GROWTH_ELITE": 899,      # SEO + Weekly Content Updates
            "SOVEREIGN_PARTNER": 2499 # Managed Ads + Lead Gen for them
        }

    def calculate_projected_mrr(self, client_count):
        # Target: 500 clients on Growth Elite = R449,500 MRR
        # Target: 100 clients on Sovereign Partner = R249,900 MRR
        return sum([self.tiers["GROWTH_ELITE"] * 500, self.tiers["SOVEREIGN_PARTNER"] * 100])
      
