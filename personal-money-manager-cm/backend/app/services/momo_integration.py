# File: /personal-money-manager-cm/personal-money-manager-cm/backend/app/services/momo_integration.py

from fastapi import HTTPException
import requests

class MoMoIntegration:
    def __init__(self, client_id: str, client_secret: str, base_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.access_token = None

    def get_access_token(self):
        url = f"{self.base_url}/v1/token"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self._encode_credentials()}"
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            self.access_token = response.json().get("access_token")
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to obtain access token")

    def _encode_credentials(self):
        import base64
        credentials = f"{self.client_id}:{self.client_secret}"
        return base64.b64encode(credentials.encode()).decode()

    def create_transaction(self, transaction_data):
        if not self.access_token:
            self.get_access_token()
        
        url = f"{self.base_url}/v1/transactions"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=transaction_data, headers=headers)
        if response.status_code != 201:
            raise HTTPException(status_code=response.status_code, detail="Failed to create transaction")
        return response.json()

    def get_transaction_status(self, transaction_id):
        if not self.access_token:
            self.get_access_token()
        
        url = f"{self.base_url}/v1/transactions/{transaction_id}"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to retrieve transaction status")
        return response.json()