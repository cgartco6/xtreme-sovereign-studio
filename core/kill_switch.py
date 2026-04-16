import os

def check_emergency_status():
    """Checks a remote 'signal' file to see if the engine should stop."""
    # You can trigger this by simply creating/deleting a file in your Supabase DB or Dropbox
    if os.path.exists("STOP_ENGINE.txt"):
        print("🚨 [EMERGENCY] Kill-switch activated. Shutting down all Agentic Workflows.")
        # Logic to kill the TMUX session or the Python process
        os._exit(1)

if __name__ == "__main__":
    check_emergency_status()
  
