from enumy.warunki_pogodowe import WarunkiPogodowe

class CzujnikDane:
    def __init__(self, temperatura: float, wilgotnosc: float, warunki: WarunkiPogodowe):
        self.temperatura = temperatura
        self.wilgotnosc = wilgotnosc
        self.warunki = warunki

    def __str__(self):
        return f"Temp: {self.temperatura}°C, Wilgotność: {self.wilgotnosc}%, Warunki pogodowe: {self.warunki.value}"
