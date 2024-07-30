import requests

def create_embbeding(text):
    try:
        url = "http://embeddingmodel_container:5000/embed"
        #url = "http://localhost:5001/embed"
        data = {"text": text}

        response = requests.post(url, json=data, timeout=10)

        if response.status_code == 200:
            vector = response.json().get("embeddings")
            return vector
        else:
            print("Error for vector:", response.status_code, response.json())
    except:
        print(f"Error with Embedding")
