from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS
from query_recommender import queryReco


app = Flask(__name__)
#CORS(app) # alle Anfraen erlauben!
#CORS(app, resources={r"/predict": {"origins": "http://webserver:80"}}) # für ausführen im Container!
#CORS(app, resources={r"/predict": {"origins": "http://127.0.0.1:5500"}}) Nur für lokale Ausführung
CORS(app, resources={r"/predict": {"origins": "*"}})


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)