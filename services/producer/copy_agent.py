import openai

class CopyAgent:
    def __init__(self):
        self.client = openai.OpenAI()

    def craft_brand_voice(self, company_name, niche):
        """Generates high-conversion website copy and taglines."""
        prompt = f"Write 3 high-conversion taglines for {company_name} in the {niche} industry. Tone: Professional, Institutional, Elite."
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
      
