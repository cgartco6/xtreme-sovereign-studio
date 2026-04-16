class GlobalArbitrage:
    """Switches markets based on timezone and currency value."""
    def __init__(self):
        self.markets = {
            "SA": {"currency": "ZAR", "price": 599, "timezone": "Africa/Johannesburg"},
            "USA": {"currency": "USD", "price": 39, "timezone": "America/New_York"},
            "UK": {"currency": "GBP", "price": 29, "timezone": "Europe/London"}
        }

    def get_optimal_market(self, current_hour_sast):
        # If it's 2 AM in SA, switch to US leads for impulse buying
        if 0 <= current_hour_sast <= 5:
            return self.markets["USA"]
        return self.markets["SA"]
      
