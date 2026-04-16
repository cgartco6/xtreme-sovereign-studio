class InfinityFunnel:
    """Ensures a non-stop rotation of 750-lead blitzes."""
    def __init__(self, targeting_ai):
        self.targeting = targeting_ai
        self.monthly_target_revenue = 1000000 # 1M ZAR

    def rotate_leads(self):
        """Clears converted leads and injects fresh impulse leads."""
        stats = self.targeting.get_stats()
        if stats['current_blitz_count'] >= 750:
            print("🔄 [INFINITY] Blitz complete. Resetting for the next 750 leads...")
            self.targeting.reset_and_scrape_new_batch()

    def track_million_progress(self, current_revenue):
        remaining = self.monthly_target_revenue - current_revenue
        print(f"📈 [REVENUE] R{current_revenue} generated. R{remaining} to hit 1M.")
      
