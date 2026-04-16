class CloserBot:
    def handle_objection(self, lead_input):
        """Autonomous responses to close the R599 sale."""
        prompts = {
            "expensive": "At R599, this site pays for itself with your first customer. It's a risk-free investment.",
            "time": "Our AI builds and deploys your site in under 24 hours. You don't wait."
        }
        # Logic to return the most aggressive high-conversion response
        return prompts.get(lead_input, "This offer is only valid for the next 48 hours.")
      
