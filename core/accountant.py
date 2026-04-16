import csv
from datetime import datetime

class DigitalAccountant:
    """Generates manual banking instructions for the Owner."""
    def __init__(self, finance_engine):
        self.finance = finance_engine

    def generate_payout_manifest(self, total_weekly_revenue):
        """Creates a CSV for easy bulk-upload or manual entry."""
        splits = self.finance.execute_split(total_weekly_revenue)
        filename = f"payouts/PAYOUT_{datetime.now().strftime('%Y_%m_%d')}.csv"
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Account Name", "Account Number", "Amount (ZAR)", "Reference"])
            writer.writerow(["FNB Main", os.getenv("FNB_ACCOUNT"), splits["payout_fnb"], "SOVEREIGN_OPS"])
            writer.writerow(["African Bank", os.getenv("AFRICAN_BANK_ACCOUNT"), splits["payout_african_bank"], "SOVEREIGN_RESERVE"])
            writer.writerow(["Growth Ledger", os.getenv("GROWTH_LEDGER_ACCOUNT"), splits["payout_growth_ledger"], "SOVEREIGN_UPGRADE"])
        
        print(f"📄 [ACCOUNTANT] Weekly Manifest generated: {filename}")
        return filename
      
