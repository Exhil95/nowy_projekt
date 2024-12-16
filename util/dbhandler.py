import sqlite3 as sql
import os
from datetime import datetime

class Baza:
    def __init__(self) -> None:
        self.plik = self._tworz_nazwe_pliku()
    
    def _tworz_nazwe_pliku(self) -> str:
        dzis: str = datetime.now().strftime("%d-%m-%Y")
        return dzis + ".db"
    
    def sprawdz_istnienie_db(self) -> bool:
        if os.path.isfile(self.plik):
            print("Baza istnieje.")
            return True
        else:
            with sql.connect(self.plik) as con:
                print("Stworzono bazę danych.")
            return False
        
    def polacz_baza(self):
        if not os.path.isfile(self.plik):
            raise FileNotFoundError(f"Baza danych '{self.plik}' nie istnieje. Użyj metody `sprawdz_istnienie_db()`.")
        return sql.connect(self.plik)

def main():
    baza = Baza()
    baza.sprawdz_istnienie_db()
    
    polaczenie = None
    
    try:
        polaczenie = baza.polacz_baza()
        print("Połączono z bazą danych:", polaczenie)
        
    except FileNotFoundError as e:
        print("Błąd:", e)
        
    finally:
        if polaczenie:
            polaczenie.close()
            print("Połączenie zostało zamknięte.")

if __name__ == "__main__":
    main()
