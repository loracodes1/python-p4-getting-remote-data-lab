# lib/GetRequester.py

import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send GET request to the URL
        response = requests.get(self.url)
        # Decode the response content to a string
        return response.content.decode("utf-8")

    def load_json(self):
        # Parse the JSON from the decoded response body
        response_body = self.get_response_body()
        return json.loads(response_body)
