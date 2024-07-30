import requests

class api_call_vec():
    def __init__(self) -> None:
         self.base_url = 'http://flask_app_container:5000/api/courses'

    def send_vector(self,vector):

        data = {
            "vector": vector
        }

        try:
            response = requests.post(f"{self.base_url}/search", json=data)
            if response.status_code == 200 and response.json():
                courses = response.json() # gives all infos of x courses
                return courses
            else:
                print(f"send_vector: status code:{response.status_code}")
        except:
            print(f"Vector request fail, Status code: {response.status_code}")
            return None