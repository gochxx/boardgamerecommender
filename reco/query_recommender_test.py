import unittest
import pandas as pd
from query_recommender import queryReco

class TestQueryReco(unittest.TestCase):

    def test_queryReco_output_format(self):
        # Testet, ob die Ausgabe im erwarteten Format ist (JSON)
        recoInputs = {
            "yearpublished": 2020,
            "playingtime": 60,
            "age": 10,
            "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"],
            "mec": ["mec_DiceRolling", "mec_ModularBoard"]
        }
        output = queryReco(recoInputs)
        self.assertIsInstance(output, str)
        self.assertTrue(output.startswith("[{") and output.endswith("}]"))

    def test_queryReco_output_content(self):
        # Testet, ob die Ausgabe die erwarteten Informationen enthält
        recoInputs = {
            "yearpublished": 2020,
            "playingtime": 60,
            "age": 10,
            "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"],
            "mec": ["mec_DiceRolling", "mec_ModularBoard"]
        }
        output = queryReco(recoInputs)
        # Hier könntest du spezifische Tests für die Inhalte der Ausgabe durchführen, je nachdem, was du erwartest

    def test_queryReco_missing_inputs(self):
        # Testet, wie die Funktion reagiert, wenn einige Inputs fehlen
        recoInputs = {
            "yearpublished": 2020,
            "playingtime": 60,
            "cat": ["cat_CardGame", "cat_ScienceFiction", "cat_Dice", "cat_Animals"],
            "mec": ["mec_DiceRolling", "mec_ModularBoard"]
        }
        with self.assertRaises(KeyError):
            queryReco(recoInputs)

if __name__ == '__main__':
    unittest.main()