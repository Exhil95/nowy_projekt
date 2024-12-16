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
    
    def utworz_tabele(self):
        with self.polacz_baza() as con:
            cursor = con.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dane (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    lokacja TEXT NOT NULL,
                    temperatura FLOAT NOT NULL,
                    wilgotnosc FLOAT NOT NULL,
                    warunki TEXT NOT NULL
                )
                           ''')
            con.commit()
            
    def dodaj_dane(self, lokacja: str, temperatura: float, wilgotnosc: float, warunki: str):
        with self.polacz_baza() as con:
            cursor = con.cursor()
            cursor.execute('''
                INSERT INTO dane (lokacja, temperatura, wilgotnosc, warunki)
                VALUES (?, ?, ?, ?)
            ''', (lokacja, temperatura, wilgotnosc, warunki))
            con.commit()
            print(f"Dodano dane: {lokacja} - {temperatura} - {wilgotnosc} - {warunki}")
            
def main():
    baza = Baza()
    baza.sprawdz_istnienie_db()
    
    baza.utworz_tabele()
    baza.dodaj_dane("polska", 12, 60, "cloudy")
    baza.dodaj_dane("japonia", 13, 90, "rainy")
    baza.dodaj_dane("iran", 14, 66, "sunny")
    # polaczenie = None
    
    # try:
    #     polaczenie = baza.polacz_baza()
    #     print("Połączono z bazą danych:", polaczenie)
        
    # except FileNotFoundError as e:
    #     print("Błąd:", e)
        
    # finally:
    #     if polaczenie:
    #         polaczenie.close()
    #         print("Połączenie zostało zamknięte.")

if __name__ == "__main__":
    main()
