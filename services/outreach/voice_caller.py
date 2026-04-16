import requests
import os

class BronwynVoice:
    """Outbound voice-cloning engine for Bronwyn."""
    def __init__(self):
        self.api_key = os.getenv("ELEVENLABS_API_KEY")
        self.voice_id = os.getenv("BRONWYN_VOICE_ID")

    def generate_sales_call_audio(self, client_name, niche):
        """Generates a high-conversion audio pitch."""
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
        payload = {
            "text": f"Hi {client_name}, this is Bronwyn from Xtreme Studio. I noticed your {niche} site isn't mobile-friendly. We can fix that for R599 today.",
            "model_id": "eleven_monolingual_v1"
        }
        headers = {"xi-api-key": self.api_key}
        response = requests.post(url, json=payload, headers=headers)
        
        output_path = f"outreach/calls/{client_name}_pitch.mp3"
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
      
