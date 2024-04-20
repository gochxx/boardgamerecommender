import unittest
import json
from reco_api import app

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        # Initialisierung des Flask-Testclients und Festlegung des Testmodus
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Testet den Home-Endpunkt der Flask-App
        response = self.app.get('/')
        # Überprüft, ob der Statuscode der Antwort 200 (OK) ist
        self.assertEqual(response.status_code, 200)
        # Überprüft, ob die zurückgegebene Nachricht "Hello, Flask!" ist
        self.assertEqual(response.data.decode('utf-8'), 'Hello, Flask!')

    def test_predict_missing_features(self):
        # Testet die Vorhersagefunktion mit fehlenden Merkmalen
        data = {}
        # Sendet eine POST-Anfrage an den '/predict'-Endpunkt mit fehlenden Merkmalen
        response = self.app.post('/predict', json=data)
        # Überprüft, ob der Statuscode der Antwort 400 (Bad Request) ist
        self.assertEqual(response.status_code, 400)
        # Überprüft, ob die Fehlermeldung für fehlende Merkmale zurückgegeben wird
        self.assertIn('Fehlende Merkmale', response.data.decode('utf-8'))

    def test_predict_with_valid_data(self):
        # Testet die Vorhersagefunktion mit gültigen Daten
        data = {
            "yearpublished": 2020,
            "playingtime": 60,
            "age": 10,
            "minplayers": 2,
            "maxplayers": 4,
            "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"],
            "mec": ["mec_DiceRolling", "mec_ModularBoard"]
        }
        # Sendet eine POST-Anfrage an den '/predict'-Endpunkt mit gültigen Daten
        response = self.app.post('/predict', json=data)
        # Überprüft, ob der Statuscode der Antwort 200 (OK) ist
        self.assertEqual(response.status_code, 200)
        # Hier könntest du weitere Tests hinzufügen, um sicherzustellen, dass die Vorhersage korrekt ist.

    def test_getdata_topcat(self):
        # Testet die Funktion zum Abrufen von Daten für 'topcat'
        data = {"data": "topcat", "len": 5}
        # Sendet eine POST-Anfrage an den '/getdata'-Endpunkt für 'topcat'
        response = self.app.post('/getdata', json=data)
        # Überprüft, ob der Statuscode der Antwort 200 (OK) ist
        self.assertEqual(response.status_code, 200)
        # Überprüft, ob die zurückgegebenen Daten die erwartete Länge haben
        json_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(json_data['data']), 5)

    def test_getdata_topmec(self):
        # Testet die Funktion zum Abrufen von Daten für 'topmec'
        data = {"data": "topmec", "len": 3}
        # Sendet eine POST-Anfrage an den '/getdata'-Endpunkt für 'topmec'
        response = self.app.post('/getdata', json=data)
        # Überprüft, ob der Statuscode der Antwort 200 (OK) ist
        self.assertEqual(response.status_code, 200)
        # Überprüft, ob die zurückgegebenen Daten die erwartete Länge haben
        json_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(json_data['data']), 3)

if __name__ == '__main__':
    unittest.main()