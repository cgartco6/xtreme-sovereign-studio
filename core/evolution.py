import json

class ContinuousEvolution:
    """System that learns and adapts without version numbers."""
    def __init__(self):
        self.memory_file = "evolution_memory.json"

    def learn_from_conversion(self, client_feedback, conversion_rate):
        """Adjusts the 'Bootstrap Factory' and 'Marketer' based on success."""
        memory = self.load_memory()
        
        # If conversion is high, reinforce the current 'Xtreme' style
        # If low, autonomously pivot the UI/UX style for the next client
        if conversion_rate < 0.10:
            memory["current_style"] = "Ultra-Minimalist"
        else:
            memory["current_style"] = "High-Enterprise-Glassmorphism"
            
        self.save_memory(memory)
        print("🔄 [EVOLUTION] System adapted to current market sentiment.")

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f: return json.load(f)
        except: return {"current_style": "Professional"}

    def save_memory(self, data):
        with open(self.memory_file, 'w') as f: json.dump(data, f)
          
