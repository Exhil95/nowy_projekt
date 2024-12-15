from modele.szklarnia import Szklarnia
from kontroler.kontroler import KontrolerSzkalrni
from util.api_klient import PogodaAPI
from util.api_key import API_KEY
  
Miasto = "Warsaw,PL"

if __name__ == "__main__":
    szklarnia = Szklarnia(nazwa="Szklarnia1")
    kontroler = KontrolerSzkalrni(szklarnia)
    api_klient = PogodaAPI(API_KEY)

    czujnik = api_klient.sprawdz_pogode(Miasto)
    print(f"Informacje Pogodowe: {czujnik}")

    kontroler.zmien_warunki(czujnik)
    print(szklarnia)
