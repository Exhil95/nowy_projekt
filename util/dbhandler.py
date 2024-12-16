import sqlite3 as sql
import os
from datetime import datetime


teraz = datetime.now()
dzis = teraz.strftime("%d-%m-%Y")
plik:str = dzis + ".db"

if os.path.isfile(plik):
    print("baza istnieje")
else:
    con = sql.connect(plik)
    print("stworzono db0")