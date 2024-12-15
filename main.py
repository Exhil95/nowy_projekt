from modele.szklarnia import Szklarnia
from kontroler.kontroler import KontrolerSzkalrni
from util.api_klient import PogodaAPI
from util.api_key import API_KEY
from enumy.lokacje import Lokalizacje
from util.menago import Manager
from util.przetwarzanie import ObslugaDanych 
  
LOCATION = Lokalizacje.algieria

if __name__ == "__main__":
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)
    manager = Manager()
    obsluga = ObslugaDanych(api_klient, manager) 


    dane_pogodowe = ObslugaDanych.zdobadz_dane_pogodowe()
    deserializowane_dane = ObslugaDanych.deserializuj_dane_pogodowe(dane_pogodowe)
    for lokation_name, dane_czujnik in deserializowane_dane.items():
       print(f"Przetwarzanie danych pogodowych dla lokalizacji: {lokation_name}")
       kontroler.zmien_warunki(dane_czujnik)
       print(szklarnia)