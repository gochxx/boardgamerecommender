# Verwende das offizielle Miniconda-Image als Basisimage
FROM continuumio/miniconda3

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen (dependencies) in den Container
COPY requirements.txt .

# Kopiere die anderen Dateien
COPY reco_api.py .
COPY query_recommender.py .

# Erstelle eine neue Conda-Umgebung und installiere die Abhängigkeiten
RUN conda create -y --name myenv --file requirements.txt

# Aktiviere die erstellte Conda-Umgebung
RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Kopiere den restlichen Anwendungscode in den Container
COPY . .

# Exponiere den Port, auf dem die Flask-Anwendung läuft
EXPOSE 5000

# Starte die Flask-Anwendung beim Ausführen des Containers
CMD ["python", "reco_app.py"]