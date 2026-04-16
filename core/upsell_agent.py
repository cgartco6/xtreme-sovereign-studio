class MillionaireUpsell:
    def trigger_upsell_sequence(self, client_id, revenue_generated):
        """Pitches high-ticket services once the client sees R599 value."""
        if revenue_generated > 0:
            return "Hi! Your new site is performing. Ready to turn on the 'Sovereign Ad Engine' to double your leads? It's R999/month, fully managed by me."
          
