class CopyFactory:
    """Generates Ads, Pamphlets, and Marketing Campaigns."""
    
    def build_campaign(self, niche, goal="Lead Gen"):
        campaign = {
            "ad_copy": "Stop losing clients to competitors. Get Sovereign branding today.",
            "pamphlet_content": "Full company history, values, and service breakdown...",
            "blog_posts": [f"Top 5 reasons {niche} needs AI branding", "Why SEO matters"],
            "marketing_strategy": "Week 1: Awareness, Week 2: Consideration, Week 3: Conversion"
        }
        return campaign
      
