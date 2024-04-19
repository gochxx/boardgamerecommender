from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
from query_recommender import queryReco


app = Flask(__name__)
#CORS(app) # alle Anfraen erlauben!
#CORS(app, resources={r"/predict": {"origins": "http://webserver:80"}}) # für ausführen im Container!
#CORS(app, resources={r"/predict": {"origins": "http://127.0.0.1:5500"}}) Nur für lokale Ausführung
CORS(app, resources={r"/predict": {"origins": "*"}})
CORS(app, resources={r"/getdata": {"origins": "*"}})


@app.route("/")
def home():
    return "Hello, Flask!"



# Dummy-Modell (Sie sollten Ihr eigenes Modell hier laden)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Daten aus der Anfrage als JSON erhalten
        
        data = request.get_json()
        
        # Überprüfen, ob die erforderlichen Merkmale im JSON vorhanden sind
        if "yearpublished" not in data or "playingtime" not in data or "age" not in data or "cat" not in data or "mec" not in data or "sub" not in data:
            return jsonify({"error": "Fehlende Merkmale"}), 400
        
        # Merkmale aus der JSON-Anfrage extrahieren
        yearpublished = int(data["yearpublished"])
        playingtime = int(data["playingtime"])
        age = int(data["age"])
        cat = data["cat"]
        mec = data["mec"]
        sub = data["sub"]
        

        # Vorhersage mit dem Modell durchführen
        ''' Dummy Data
        myInputs = {"yearpublished": 2020, "playingtime": 60, "age": 10, 
              "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"], 
              "mec": ["mec_DiceRolling", "mec_ModularBoard"]}
        '''
        myInputs = {"yearpublished": yearpublished, "playingtime": playingtime, "age": age, "sub": sub,
              "cat": cat, "mec": mec}
        
        prediction = queryReco(myInputs)
        #predictionout = str(prediction[0])
        # Die Vorhersage als JSON-Antwort senden
        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/getdata", methods=["POST"])
def getdata():
    try:
        json = request.get_json()
        data = json["data"]
        len = json["len"]
        print(data)
        file_path = ""
        # Der Dateipfad, aus dem die Daten gelesen werden sollen
        if (data=="topcat"):
            file_path = 'data/topcat.txt'
        elif(data=="topmec"):
            file_path = 'data/topmec.txt'
        # Eine leere Liste erstellen, um die Daten zu speichern
        

        # Die Textdatei öffnen und im Lesemodus ('r') öffnen
        with open(file_path, 'r') as file:
            # Jede Zeile der Datei lesen und der Liste hinzufügen
            for line in file:
                # Die Zeile nach Kommas trennen und die Werte zur Liste hinzufügen
                data_list= line.strip().split(',')

        # Führende "cat" entfernen
        return jsonify({"data": data_list[:len]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)