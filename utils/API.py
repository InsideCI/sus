import json
import requests


class API:
    def __init__(self, address):
        self.address = address

    def post(self, body, endpoint):
        if len(body) != 0:
            for element in body:
                data = json.dumps(element, ensure_ascii=False).encode('utf-8')
                print(data)
                requests.post(self.address + endpoint, data=data)
