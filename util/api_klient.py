import requests
from enumy.warunki_pogodowe import WarunkiPogodowe
from modele.czujnik_szklarnia import CzujnikDane

class PogodaAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://api.weatherapi.com/v1/current.json"

    def sprawdz_pogode(self, miasto: str) -> CzujnikDane:
        parametry = {"key": self.api_key, "q": miasto}
        odpowiedz = requests.get(self.url, params=parametry)
        data = odpowiedz.json()
        warunki = WarunkiPogodowe[data['current']['condition']['text'].upper()]
        return CzujnikDane(
            temperatura=data['current']['temp_c'],
            wilgotnosc=data['current']['humidity'],
            warunki=warunki
        )
