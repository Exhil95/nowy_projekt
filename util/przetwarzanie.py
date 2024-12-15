from enumy.lokacje import Lokalizacje
from modele.czujnik_szklarnia import CzujnikDane
from enumy.warunki_pogodowe import WarunkiPogodowe
from util.menago import Manager

class ObslugaDanych:
    def __init__(self, api_klient, manager: Manager):
        self.api_klient = api_klient
        self.manager = manager
    
    def zdobadz_dane_pogodowe(self):
        dane_pogodowe = self.manager.zdobadz_dane_pogodowe()
        if dane_pogodowe is None:
            dane_pogodowe = {}
            
            for lokation in Lokalizacje:
                print(f"Zdobywanie danych dla: {lokation.name} ({lokation.value})")
                try:
                    dane_czujnik = self.api_klient.zdobyj_dane_pogodowe(lokation.value)
                    print(f"Dane pogodowe:{dane_czujnik}")
                    dane_pogodowe[lokation.name] = {
                        "temperature": dane_czujnik.temperature,
                        "humidity": dane_czujnik.humidity,
                        "condition": dane_czujnik.condition,
                    }
                except Exception as e:
                    print(f"Błąd: {e}")
            
            self.manager.zapisz(dane_pogodowe)
        return dane_pogodowe
    
    def deserializuj_dane_pogodowe(self, dane_pogodowe):
        deserializowane_dane = {}
        for lokation_name, data in dane_pogodowe.items():
            deserializowane_dane[lokation_name] = CzujnikDane(
                 temperature=data["temperature"],
                humidity=data["humidity"],
                condition=WarunkiPogodowe(data["condition"])
            )
        return deserializowane_dane
