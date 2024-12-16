from modele.szklarnia import Szklarnia
from kontroler.kontroler import KontrolerSzkalrni
from util.api_klient import PogodaAPI
from util.api_key import API_KEY
from enumy.lokacje import Lokalizacje
import time
from util.dbhandler import Baza

def main() -> None:
    start = time.perf_counter()
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)
    baza = Baza()
    baza.sprawdz_istnienie_db()
    baza.utworz_tabele()

    for miasta in Lokalizacje:
        print(f"Sprawdzanie danych w {miasta.name}")
        czujnik = api_klient.sprawdz_pogode(miasta.value)
        baza.dodaj_dane(miasta.name, czujnik.temperatura, czujnik.wilgotnosc, czujnik.warunki.name)
        print(f"Informacje Pogodowe: {czujnik}")
        kontroler.zmien_warunki(czujnik)
        print(szklarnia)
        
    finish = time.perf_counter()
    wynik = round(finish - start, 2)
    print(f"Zakończono w czasie {wynik} sekund(y)")


def test_main() -> None:
    start = time.perf_counter()
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)
    baza = Baza()
    
    if not baza.sprawdz_istnienie_db():
        baza.utworz_tabele()
        for miasta in Lokalizacje:
            print(f"Sprawdzanie danych w {miasta.name}")
            czujnik = api_klient.sprawdz_pogode(miasta.value)
            baza.dodaj_dane(miasta.name, czujnik.temperatura, czujnik.wilgotnosc, czujnik.warunki.name)
            print(f"Informacje Pogodowe: {czujnik}")
            kontroler.zmien_warunki(czujnik)
            print(szklarnia)
    else:
        for miasta in Lokalizacje:
            print("Odczyt z bazy")
    
    finish = time.perf_counter()
    wynik = round(finish - start, 5)
    print(f"Zakończono w czasie {wynik} sekund(y)")
          
if __name__ == "__main__":
    # main()
    test_main()