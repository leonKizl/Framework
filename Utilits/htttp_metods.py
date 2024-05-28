import requests
import allure
from Utilits.logger import Logger
class http_metod():
    headers = {'Content-Type':'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url,method="GET")
            result = requests.get(url,headers=http_metod.headers,cookies=http_metod.cookie)
            Logger.add_response(result)
            return result
    
    @staticmethod
    def post(url,body):
        with allure.step("POST"):
            Logger.add_request(url,method="POST")
            result = requests.post(url,json=body,headers=http_metod.headers,cookies=http_metod.cookie)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url,body):
        with allure.step("PUT"):
            Logger.add_request(url,method="PUT")
            result = requests.put(url,json=body,headers=http_metod.headers,cookies=http_metod.cookie)
            Logger.add_response(result)
            return result
    
    @staticmethod
    def delete(url,body):
        with allure.step("Delete"):
            Logger.add_request(url,method="Delete")
            result = requests.delete(url,json=body,headers=http_metod.headers,cookies=http_metod.cookie)
            Logger.add_response(result)
            return result