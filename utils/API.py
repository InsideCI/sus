import json
import requests

JWT = ""

headers = {
    "Authorization": f"BEARER {JWT}"
}


class API:
    def __init__(self, address):
        self.address = address

    def post(self, body, endpoint):
        if len(body) != 0:
            data = json.dumps(body, ensure_ascii=False).encode('utf-8')
            print(f"POST: {data} to {endpoint}. Status = ", end="")
            response = requests.post(self.address + endpoint,
                                     data=data, headers=headers)
            print(response.status_code)
