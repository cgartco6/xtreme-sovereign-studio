import smtplib
from email.mime.text import MIMEText

class HunterMailer:
    def __init__(self, smtp_user, smtp_pass):
        self.user = smtp_user
        self.passw = smtp_pass

    def send_high_conversion_pitch(self, lead_email, company_name):
        """A clean, professional, no-fluff pitch."""
        subject = f"Rebranding {company_name} | High-Enterprise Digital Assets"
        body = f"""
Hello,

I noticed your current digital presence doesn't match the scale of your operations. 

We specialize in autonomous, high-enterprise branding. We've already generated a preliminary concept for {company_name} using our Sovereign Engine.

You can view the direction and secure the assets here: [Your Storefront Link]

No fluff. Just real quality.

Best,
The Xtreme Studio Bot
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = lead_email

        # Logic to connect to SMTP and fire
        print(f"Pitch deployed to {lead_email}")
      
