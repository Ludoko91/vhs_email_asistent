import requests

from utils.quene import email_queue

class mail_processing():

    def strip_mail(self):
        x = email_queue.get()
        body = x[2]
        text_n = body.replace("/n","")
        text = text_n.replace("  ","")
        data = {
            "from_": x[0],
            "subject": x[1],
            "message": text,
            "message_vector": None,
            "subject_vector": None,

        }
        return data
    
    def create_embbeding(self,text):
        try:
            url = "http://embeddingmodel_container:5000/embed"
            data = {"text": text}

            response = requests.post(url, json=data, timeout=10)

            if response.status_code == 200:
                vector = response.json().get("embeddings")
                return vector
            else:
                print("Error for vector:", response.status_code, response.json())
        except:
            print(f"Error with Embedding")
