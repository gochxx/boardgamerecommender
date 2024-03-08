import requests
import json


url = "http://192.168.178.26:5000/predict"  # Stellen Sie sicher, dass die Adresse und der Port korrekt sind
data = {
    "feature1": 5.1,
    "feature2": 3.5,
    "feature3": 8.4,
    "feature4": 5.2
}
data = {"yearpublished": 2020, "playingtime": 60, "age": 10, 
              "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"], 
              "mec": ["mec_DiceRolling", "mec_ModularBoard"]}

headers = {'Content-Type': 'application/json'}


response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print("Vorhersage:", result["prediction"])
else:
    print("Fehler:", response.status_code, response.text)

