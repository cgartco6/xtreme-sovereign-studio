from core.vault import DigitalVault

vault = DigitalVault()

@app.route('/api/release-assets', methods=['POST'])
@require_api_key
def release_assets():
    data = request.json
    email = data.get('email')
    
    # Logic to package DesignAgent and CopyAgent outputs into a ZIP
    token = vault.generate_secure_token(email)
    
    # Send email with the vault link
    print(f"Digital Assets Unlocked. Vault Token: {token} sent to {email}")
    return jsonify({"status": "released", "vault_token": token})
  
