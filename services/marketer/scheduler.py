import time

class SovereignScheduler:
    def __init__(self):
        self.algo = MarketAlgorithm()
        self.creator = ContentCreator()

    def run_automation_loop(self):
        print("🚀 Marketing Automation: ONLINE")
        while True:
            for platform in ["Facebook", "Instagram", "TikTok", "LinkedIn"]:
                if self.algo.should_post_now(platform):
                    content = self.creator.create_ad_campaign("Sovereign Studio")
                    # Logic to call Social Media APIs (Meta, TikTok, LinkedIn)
                    print(f"[POSTED] Content pushed to {platform} at peak engagement.")
            
            # Sleep for 1 minute before next check
            time.sleep(60)
          
