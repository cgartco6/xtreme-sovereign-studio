import os
import uuid
from datetime import datetime, timedelta

class DigitalVault:
    """Manages secure access to generated branding assets."""
    def __init__(self):
        self.storage_path = "./vault/assets"
        os.makedirs(self.storage_path, exist_ok=True)

    def generate_secure_token(self, project_id):
        """Creates a unique access key for the digital download."""
        return str(uuid.uuid4())

    def get_download_link(self, token):
        """Returns the internal path to the zip/package."""
        # In production, this would point to an S3 Signed URL
        return f"/api/download/{token}"
      
