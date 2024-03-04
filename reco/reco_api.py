from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://127.0.0.1:5500"}})



@app.route("/")
def home():
    return "Hello, Flask!"


# Dummy-Modell (Sie sollten Ihr eigenes Modell hier laden)
'''
model = joblib.load("knn_iris.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Daten aus der Anfrage als JSON erhalten
        data = request.get_json()
        
        # Überprüfen, ob die erforderlichen Merkmale im JSON vorhanden sind
        if "feature1" not in data or "feature2" not in data or "feature3" not in data or "feature4" not in data:
            return jsonify({"error": "Fehlende Merkmale"}), 400
        
        # Merkmale aus der JSON-Anfrage extrahieren
        feature1 = float(data["feature1"])
        feature2 = float(data["feature2"])
        feature3 = float(data["feature3"])
        feature4 = float(data["feature4"])
        
        # Vorhersage mit dem Modell durchführen
        prediction = model.predict([[feature1, feature2, feature3, feature4]])
        predictionout = int(prediction[0])
        # Die Vorhersage als JSON-Antwort senden
        return jsonify({"prediction": predictionout})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)