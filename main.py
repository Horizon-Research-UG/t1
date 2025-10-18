print("Starte Hauptprogramm...\n")
# Importiere das Log-Modul
from timeit import main
import log
# Erstelle automatisch einen Log-Eintrag
log.log_call()

import time # lädt das time-Modul

time.sleep(2) # pausiert das Programm für 2 Sekunden
a = 3
print("\n"*a)


######################################################





# Importiere das Menü-Modul
import menu
def main():
    menu.starte_menu()


if __name__ == "__main__":
    main()






######################################

print("Speichern und beenden des Hauptprogramms...\n")
log.log_call()  # Aktualisiert die log variable





# "Carpe diem - Nutze den Tag!" - Horaz