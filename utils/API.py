import json
import requests


class API:
    def __init__(self, address):
        self.address = address

    def post(self, body, endpoint):
        if len(body) != 0:
            data = json.dumps(body, ensure_ascii=False).encode('utf-8')
            requests.post(self.address + endpoint, data=data)
