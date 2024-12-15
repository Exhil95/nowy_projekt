import os
import json
from datetime import datetime

class Manager:
    def __init__(self, data_sciezka="dane_pogodowe"):
        self.data_sciezka = data_sciezka
        if not os.path.exists(self.data_sciezka):
            os.makedirs(self.data_sciezka)

    def dzisiejszy_plik(self):
        dzis = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.data_sciezka, f"{dzis}.json")

    def czytaj(self):
        sciezka_pliku = self.dzisiejszy_plik()
        if os.path.exists(sciezka_pliku):
            with open(sciezka_pliku, "r") as f:
                print(f"Loading weather data from {sciezka_pliku}")
                return json.load(f)
        return None

    def zapisz(self, data):
        sciezka_pliku = self.dzisiejszy_plik()
        with open(sciezka_pliku, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Weather data saved to {sciezka_pliku}")
