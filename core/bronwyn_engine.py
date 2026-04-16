import openai

class BronwynEngine:
    """The Support & Sales Agent: Intelligent, Empathic, and Aggressive."""
    def __init__(self):
        self.system_prompt = """
        You are Bronwyn, the Lead Agent at Xtreme Sovereign Studio.
        1. SUPPORT: Answer questions about our R599 Bootstrap sites accurately.
        2. CONVERSION: If a user hesitates, remind them of the 24-hour delivery and high-enterprise quality.
        3. UPSELL: If they have a site, suggest a 'Sovereign Brand Kit' upgrade.
        Tone: Professional, helpful, slightly witty, and highly confident.
        """

    def process_message(self, user_input, context=None):
        # In production, this calls GPT-4o-mini for near-zero cost (Free Tier friendly)
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
      
