from modele.szklarnia import Szklarnia
from kontroler.kontroler import KontrolerSzkalrni
from util.api_klient import PogodaAPI
from util.api_key import API_KEY
from enumy.lokacje import Lokalizacje
import time

def main() -> None:
    start = time.perf_counter()
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)

    for miasta in Lokalizacje:
        print(f"Sprawdzanie danych w {miasta.name}")
        czujnik = api_klient.sprawdz_pogode(miasta.value)
        print(f"Informacje Pogodowe: {czujnik}")

        kontroler.zmien_warunki(czujnik)
        print(szklarnia)
        
    finish = time.perf_counter()
    wynik = round(finish - start, 2)
    print(f"Zakończono w czasie {wynik} sekund")
        
if __name__ == "__main__":
    main()