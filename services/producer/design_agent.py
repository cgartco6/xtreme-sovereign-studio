import openai

class DesignAgent:
    def __init__(self):
        self.client = openai.OpenAI()

    def generate_branding_package(self, company_name, description):
        """Generates high-enterprise logos via DALL-E 3."""
        prompt = f"Professional High-Enterprise minimalist logo for {company_name}, {description}. Clean, addictive UX aesthetic, deep blues and silver."
        
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
      
