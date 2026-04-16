class PayoutEngine:
    def execute_split(self, amount_zar):
        """Strictly calculates the ZAR values for your manual Friday transfers."""
        return {
            "fnb_ops": amount_zar * 0.30,
            "african_bank_savings": amount_zar * 0.20,
            "growth_system_upgrades": amount_zar * 0.50
        }
      
