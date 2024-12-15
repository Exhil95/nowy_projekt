class Szklarnia:
    def __init__(self, nazwa: str):
        self.nazwa = nazwa
        self.temperatura = 22.0  # domyslna temperatura (celsjusz)
        self.wilgotnosc = 50.0    # domyslna wilgotnosc w %

    def dostosuj_warunki(self, docelowa_temperatura: float, docelowa_wilgotnosc: float):
        self.temperatura = docelowa_temperatura
        self.wilgotnosc = docelowa_wilgotnosc

    def __str__(self):
        return f"Szklarnia: {self.nazwa}: Temperatura: {self.temperatura}°C, Wilgotność: {self.wilgotnosc}%"
