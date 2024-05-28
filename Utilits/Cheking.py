
import json
from requests import Response


class Checking_status():

    @staticmethod
    def check_status_code(response:Response,status_code):
        assert response.status_code == status_code
        if status_code == response.status_code:
            print(f"Status code {response.status_code}")
        else:
            print(f"Status code is not right! -\n{response.status_code}")

    @staticmethod
    def check_json_token(response:Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("OK: Response has all expected values")

