import os
import time
from core.style_brain import StyleBrain
from services.producer.media_exporter import MediaExporter

class ContentPipeline:
    """Automated Ghost-Inbound Content Engine."""
    
    def __init__(self):
        self.style = StyleBrain()
        self.exporter = MediaExporter()
        self.output_dir = "web/public/ghost_content"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_daily_blitz(self, niche="High-Enterprise Digital Studio"):
        """Creates 1 set of professional content for TikTok, LinkedIn, and X."""
        print(f"🚀 [GHOST] Generating inbound content for: {niche}")
        
        # 1. VISUAL: Generate a 4K Vertical Ad (Simulated logic call to DesignStudio)
        # In 2026, we use HEVC (H.265) for maximum quality on mobile.
        video_path = f"{self.output_dir}/daily_ad_{int(time.time())}.mp4"
        self.exporter.export_video_social(source="raw_assets/studio_preview.mov", output=video_path)

        # 2. COPY: High-Trust, Professional Hooks (Classic/Futuristic styles)
        hooks = {
            "LinkedIn": f"The future of {niche} isn't human-only. It's Sovereign. [Link in Bio]",
            "TikTok": f"POV: You found the only studio that delivers 4K vectors in 120s. 🇿🇦 #SovereignStudio",
            "X": f"Stop paying for mid-tier design. Scale with high-enterprise automation. 🚀"
        }

        # 3. SCHEDULE: Prepares metadata for social_ghost.py to upload
        return {"video": video_path, "copy": hooks, "status": "Ready to Post"}

if __name__ == "__main__":
    pipeline = ContentPipeline()
    package = pipeline.generate_daily_blitz()
    print(f"✅ Content Package Created: {package['status']}")
  
