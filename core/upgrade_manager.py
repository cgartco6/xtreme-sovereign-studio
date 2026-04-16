class UpgradeManager:
    def __init__(self):
        self.upgrade_tiers = {
            "CRITICAL": [{"id": "C1", "name": "AI Cluster Expansion", "cost": 50000}],
            "MAJOR": [{"id": "MA1", "name": "Voice-Agent Integration", "cost": 15000}],
            "MINOR": [{"id": "MI1", "name": "UI/UX Smoothing", "cost": 2500}]
        }

    def get_available_upgrades(self, current_growth_balance):
        """Lists what can be bought right now using the 50% Growth Fund."""
        available = []
        for tier, items in self.upgrade_tiers.items():
            for item in items:
                if current_growth_balance >= item["cost"]:
                    available.append({"tier": tier, **item})
        return available
      
