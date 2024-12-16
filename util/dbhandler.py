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
                    nazwa TEXT NOT NULL,
                    wartosc INTEGER NOT NULL
                )
                           ''')
            con.commit()
            
    def dodaj_dane(self, nazwa: str, wartosc: int):
        with self.polacz_baza() as con:
            cursor = con.cursor()
            cursor.execute('''
                INSERT INTO dane (nazwa, wartosc)
                VALUES (?, ?)
            ''', (nazwa, wartosc))
            con.commit()
            print(f"Dodano dane: {nazwa} - {wartosc}")

def main():
    baza = Baza()
    baza.sprawdz_istnienie_db()
    
    baza.utworz_tabele()
    baza.dodaj_dane("Przykład 1", 123)
    baza.dodaj_dane("Przykład 2", 456)
    baza.dodaj_dane("Przykład 3", 789)
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
