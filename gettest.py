from utils.quene import question_vector_queue
import json
import os

def i(mail):

    data = {
        "email": mail

    }
    # Angepasster Ordnerpfad für die JSON-Datei
    folder_path = "Json"
    os.path.dirname(os.path.abspath(__file__))

    # Angepasster Dateiname für die JSON-Datei
    file_name = "test" + '.json'

    # Erstelle den vollständigen Pfad zur JSON-Datei
    file_path = os.path.join(folder_path, file_name)
    # Speichere das Python-Wörterbuch als JSON-Datei
    with open(file_path, 'w') as file:
        json.dump(data, file)
    