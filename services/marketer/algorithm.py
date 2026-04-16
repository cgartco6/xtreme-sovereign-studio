from datetime import datetime
import pytz

class MarketAlgorithm:
    """Advanced timing engine for South African Engagement."""
    def __init__(self):
        self.tz = pytz.timezone('Africa/Johannesburg')
        # Algorithmic peaks based on 2026 SA data
        self.platform_rules = {
            "Facebook": {"peak": "09:00", "days": ["Wednesday", "Thursday"], "limit": 3},
            "Instagram": {"peak": "18:00", "days": ["Monday", "Tuesday", "Wednesday"], "limit": 2},
            "TikTok": {"peak": "20:00", "days": ["Friday", "Saturday", "Sunday"], "limit": 5},
            "LinkedIn": {"peak": "15:00", "days": ["Wednesday", "Thursday"], "limit": 1}
        }

    def should_post_now(self, platform):
        now = datetime.now(self.tz)
        current_day = now.strftime("%A")
        current_time = now.strftime("%H:%M")
        
        config = self.platform_rules.get(platform)
        if current_day in config["days"] and current_time == config["peak"]:
            return True
        return False
      
