from Utilits.htttp_metods import http_metod

base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"


class Google_maps_api():
    
    @staticmethod
    def create_new_place():

        json_for_post = {
            "location": { 
            "lat": -38.383494, 
            "lng": 33.427362 
              }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
            "shoe park", 
            "shop"
            ],
            "website": "http://google.com", 
            "language": "French-IN"
            }
        resource_post = "/maps/api/place/add/json"
        post_url = base_url + resource_post + key
        result_post = http_metod.post(post_url,json_for_post)
        print(post_url)
        print(result_post.text)
        return result_post
    @staticmethod
    def get_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = http_metod.get(get_url)
        print(result_get.text)
        return result_get
        
    @staticmethod
    def update_place(place_id):

        json_for_put = {
            "place_id":place_id,
            "address":"SWINSKA ULICA",
            "key":"qaclick123"
        } 
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = http_metod.put(put_url,json_for_put)
        print(result_put.text)
        return result_put
    @staticmethod
    def delete_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        json_for_delete = {
            "place_id":place_id
        }
        del_url = base_url +delete_resource + key
        result_del = http_metod.delete(del_url,json_for_delete)
        print(result_del.text)
        return result_del

