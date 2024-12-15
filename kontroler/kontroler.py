from modele.szklarnia import Szklarnia
from modele.czujnik_szklarnia import CzujnikDane
from enumy.warunki_pogodowe import WarunkiPogodowe

class KontrolerSzkalrni:
    def __init__(self, szklarnia: Szklarnia):
        self.szklarnia = szklarnia

    def zmien_warunki(self, CzujnikDane: CzujnikDane):
        if CzujnikDane.warunki == WarunkiPogodowe.slonecznie:
            self.szklarnia.dostosuj_warunki(25.0, 40.0)
        elif CzujnikDane.warunki == WarunkiPogodowe.deszczowo:
            self.szklarnia.dostosuj_warunki(20.0, 60.0)
        elif CzujnikDane.warunki == WarunkiPogodowe.pochmurnie:
            self.szklarnia.dostosuj_warunki(22.0, 50.0)
        elif CzujnikDane.warunki == WarunkiPogodowe.snieznie:
            self.szklarnia.dostosuj_warunki(18.0, 40.0)
        elif CzujnikDane.warunki == WarunkiPogodowe.czesciowe_zachmurzenie:
            self.szklarnia.dostosuj_warunki(21.0, 55.0)
        else:
            self.szklarnia.dostosuj_warunki(20.0, 50.0)
