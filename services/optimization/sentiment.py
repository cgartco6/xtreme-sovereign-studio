class SentimentAnalyzer:
    """Analyzes lead intent to prioritize the 750-client target."""
    
    def analyze_reply(self, text):
        keywords_hot = ["how much", "send link", "interested", "yes"]
        text_lower = text.lower()
        
        if any(word in text_lower for word in keywords_hot):
            return "HOT_LEAD"
        return "COLD_LEAD"
      
