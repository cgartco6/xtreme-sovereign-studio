import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.marketer.scheduler import SovereignScheduler

def main():
    print("--- STARTING AGGRESSIVE MARKETING DAEMON ---")
    print("Status: Monitoring Platform Rules & Peak SAST Times...")
    
    scheduler = SovereignScheduler()
    try:
        scheduler.run_automation_loop()
    except KeyboardInterrupt:
        print("Marketing Engine Paused.")

if __name__ == "__main__":
    main()
  
