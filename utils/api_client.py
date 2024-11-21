import requests, os
from dotenv import load_dotenv

load_dotenv()

class APIClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=self.headers)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=self.headers)

    def put(self, endpoint, data=None):
        return requests.put(f"{self.base_url}{endpoint}", json=data, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)
