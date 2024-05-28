import json
from requests import Response
from Utilits.api_1 import Google_maps_api
from Utilits.Cheking import Checking_status

import allure


@allure.epic("Test create place")

class Test_create_place():

    @allure.description("Test create, update, delete place")
    def test_create_new_place(self):
        print("POST")
        result_post: Response = Google_maps_api.create_new_place()
        check_information = result_post.json()
        place_id = check_information.get("place_id")
        Checking_status.check_status_code(result_post,200)
        Checking_status.check_json_token(result_post,['status', 'place_id', 'scope', 'reference', 'id'])
    
        print("Get - Post")
        result_get = Google_maps_api.get_place(place_id)
        Checking_status.check_status_code(result_get,200)
        Checking_status.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("Put")
        result_put = Google_maps_api.update_place(place_id)
        Checking_status.check_status_code(result_put,200)
        Checking_status.check_json_token(result_put,['msg'])

        print("Get - PUT")
        result_get = Google_maps_api.get_place(place_id)
        Checking_status.check_status_code(result_put,200)
        Checking_status.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print("Delete")
        result_del = Google_maps_api.delete_place(place_id)
        Checking_status.check_status_code(result_del,200)
        Checking_status.check_json_token(result_del,['status'])

        print("Delete 2222222")
        result_del = Google_maps_api.delete_place(place_id)
        Checking_status.check_status_code(result_del,404)
        Checking_status.check_json_token(result_del,['msg'])



        print("Get - Delete")
        result_get = Google_maps_api.get_place(place_id)
        Checking_status.check_status_code(result_get,404)
        Checking_status.check_json_token(result_get,['msg'])



