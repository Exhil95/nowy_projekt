from modele.szklarnia import Szklarnia
from kontroler.kontroler import KontrolerSzkalrni
from util.api_klient import PogodaAPI
from util.api_key import API_KEY
from enumy.lokacje import Lokalizacje
import time
from util.dbhandler import Baza
from modele.czujnik_szklarnia import CzujnikDane
from enumy.warunki_pogodowe import WarunkiPogodowe

def main() -> None:
    start = time.perf_counter()
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)
    baza = Baza()
   
    
    if not baza.sprawdz_istnienie_db():
        baza.utworz_tabele()
        for miasta in Lokalizacje:
            print(f"Sprawdzanie danych w {miasta.value}")
            czujnik = api_klient.sprawdz_pogode(miasta.value)
            baza.dodaj_dane(miasta.value, czujnik.temperatura, czujnik.wilgotnosc, czujnik.warunki.value)
            print(f"Informacje Pogodowe: {czujnik}")
            kontroler.zmien_warunki(czujnik)
            print(szklarnia)
    else:
        dane_baza:list = baza.pobierz_dane()
        for i in dane_baza:
            print(f"Sprawdzanie danych z bazy w {i[0]}")
            a = WarunkiPogodowe(i[3])
            czujnik = CzujnikDane(temperatura=i[1], wilgotnosc=i[2], warunki=a)
            print(f"Informacje Pogodowe: {czujnik}")
            kontroler.zmien_warunki(czujnik)
            print(szklarnia)
            
    
    finish = time.perf_counter()
    wynik = round(finish - start, 5)
    print(f"Zakończono w czasie {wynik} sekund(y)")
          
if __name__ == "__main__":
    main()
    