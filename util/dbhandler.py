import sqlite3 as sql
import os
from datetime import datetime

class Baza:
    def __init__(self) -> None:
        self.plik = self._tworz_nazwe_pliku()
    
    def _tworz_nazwe_pliku(self) -> str:
        dzis:str = datetime.now().strftime("%d-%m-%Y")
        return dzis + ".db"
    
    def sprawdz_istnienie_db(self) -> bool:
        if os.path.isfile(self.plik):
            print("baza istnieje.")
            return False
        else:
            with sql.connect(self.plik) as con:
                print("stworzono bazę danych.")
            return True
        
    def polacz_baza(self) -> None:
        if not self.sprawdz_istnienie_db():
            raise FileNotFoundError(f"Baza danych '{self.plik}'nie istnieje, użyj metody sprawdz_istnienie_db()")
        return sql.connect(self.plik)