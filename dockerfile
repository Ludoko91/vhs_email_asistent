# Verwenden Sie ein offizielles Python-Image als Basisimage
FROM python:3.9-slim

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app 

# Kopieren Sie Ihre Anwendung in den Container
COPY . /app

# Installieren Sie notwendige Python-Pakete
RUN pip install --no-cache-dir -r requirements.txt

# Standardbefehl zum Ausführen des Containers
CMD ["python3", "run.py"]