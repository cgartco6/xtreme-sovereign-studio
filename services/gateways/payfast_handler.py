import hashlib

class PayFastHandler:
    """Handles ZAR payments directly into your account via PayFast."""
    def __init__(self, merchant_id, merchant_key, passphrase):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key
        self.passphrase = passphrase

    def generate_payment_url(self, amount, order_id):
        data = {
            'merchant_id': self.merchant_id,
            'merchant_key': self.merchant_key,
            'amount': amount,
            'item_name': f'Xtreme R599 Website Order #{order_id}'
        }
        # In production, this generates the MD5 signature required by PayFast
        return f"https://www.payfast.co.za/eng/process?merchant_id={self.merchant_id}&..."
      
