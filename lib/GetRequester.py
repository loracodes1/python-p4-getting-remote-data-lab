# lib/GetRequester.py
import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Return the raw bytes to match the test's expectation
        return requests.get(self.url).content

    def load_json(self):
        # Decode and convert JSON data into Python objects
        return requests.get(self.url).json()
