from enumy.warunki_pogodowe import WarunkiPogodowe

class CzujnikDane:
    def __init__(self, temperatura: float, wigotnosc: float, warunki: WarunkiPogodowe):
        self.temperatura = temperatura
        self.wigotnosc = wigotnosc
        self.warunki = warunki

    def __str__(self):
        return f"Temp: {self.temperatura}°C, Wilgotność: {self.wigotnosc}%, Warunki pogodowe: {self.warunki.value}"
