import requests
from enumy.warunki_pogodowe import WarunkiPogodowe
from modele.czujnik_szklarnia import CzujnikDane

class PogodaAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://api.weatherapi.com/v1/current.json"

    def sprawdz_pogode(self, location: str) -> CzujnikDane:
        try:
            parametry = {"key": self.api_key, "q": location}
            odpowiedz = requests.get(self.url, params=parametry)
            odpowiedz.raise_for_status()
            data = odpowiedz.json()
            
            if 'current' not in data:
                raise KeyError(f"Odpowiedź nie zawiera 'current': {data}")
            
            try:
                warunki = WarunkiPogodowe[data['current']['condition']['text'].lower().replace(" ", "_")]
            except ValueError:
                warunki = WarunkiPogodowe.cloudy
            
            return CzujnikDane(
                temperatura=data['current']['temp_c'],
                wilgotnosc=data['current']['humidity'],
                warunki=warunki
            )
        except KeyError as e:
            raise ValueError(f"Niepoprawna struktura: {e}")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Nieudana próba sprawdzenia pogody: {e}")

