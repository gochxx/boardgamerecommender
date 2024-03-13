# Verwende das offizielle Miniconda-Image als Basisimage
FROM continuumio/miniconda3

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anforderungen (dependencies) in den Container
COPY reco/requirements.txt reco/

VOLUME /app/data

# Kopiere die anderen Dateien
COPY reco/reco_api.py reco/
COPY reco/query_recommender.py reco/

# Erstelle eine neue Conda-Umgebung und installiere die Abhängigkeiten
RUN conda create -y --name myenv --file reco/requirements.txt

# Aktiviere die erstellte Conda-Umgebung
RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Exponiere den Port, auf dem die Flask-Anwendung läuft
EXPOSE 5000

# Starte die Flask-Anwendung beim Ausführen des Containers
CMD ["python", "reco/reco_api.py"]