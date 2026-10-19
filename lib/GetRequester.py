import requests
import json

class GetRequester:

    def __init__(self, url="https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        body = self.get_response_body()
        return json.loads(body)