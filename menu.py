# Importiere das Log-Modul für die Aufruf-Protokollierung
import log

# Protokolliere den Aufruf dieser Menü-Datei
log.log_call()

def zeige_hauptmenu():
    """Zeigt das Hauptmenü mit allen verfügbaren Optionen"""
    # Zeige eine leere Zeile für bessere Übersichtlichkeit
    print()
    # Zeige den Hauptmenü-Titel
    print("=== NEUROGAMES HAUPTMENÜ ===")
    # Zeige alle verfügbaren Menüpunkte
    print("1. Spielen")
    print("2. Einstellungen")
    print("3. Intro abspielen")
    print("4. Beenden")
    # Zeige eine Trennlinie
    print("=" * 28)

def zeige_spiel_menu():
    """Zeigt das Untermenü für Spiel-Optionen"""
    # Zeige eine leere Zeile für bessere Übersichtlichkeit
    print()
    # Zeige den Spiel-Menü-Titel
    print("=== SPIEL OPTIONEN ===")
    # Zeige alle verfügbaren Spiel-Optionen
    print("1. Neues Spiel starten")
    print("2. Schnelles Spiel")
    print("3. Spiel laden")
    print("4. Spiel erstellen")
    print("5. Tutorial starten")
    print("6. Zurück zum Hauptmenü")
    # Zeige eine Trennlinie
    print("=" * 21)

def hole_benutzer_eingabe():
    """Fragt den Benutzer nach seiner Menü-Auswahl"""
    # Frage den Benutzer nach seiner Wahl
    eingabe = input("Ihre Wahl: ")
    # Gib die Eingabe zurück
    return eingabe

def verarbeite_hauptmenu_wahl(wahl):
    """Verarbeitet die Benutzer-Auswahl im Hauptmenü"""
    # Prüfe welche Option gewählt wurde
    if wahl == "1":
        # Zeige das Spiel-Untermenü
        zeige_spiel_menu()
        # Hole die Spiel-Menü-Wahl
        spiel_wahl = hole_benutzer_eingabe()
        # Verarbeite die Spiel-Menü-Wahl
        verarbeite_spiel_wahl(spiel_wahl)
    elif wahl == "2":
        # Zeige Einstellungen-Nachricht
        print("Einstellungen werden geladen...")
    elif wahl == "3":
        # Spiele das Intro ab
        print("Intro wird abgespielt...")
    elif wahl == "4":
        # Beende das Programm
        print("Auf Wiedersehen!")
        return False
    else:
        # Zeige Fehlermeldung bei ungültiger Eingabe
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")
    # Gib True zurück um das Menü weiterlaufen zu lassen
    return True

def verarbeite_spiel_wahl(wahl):
    """Verarbeitet die Benutzer-Auswahl im Spiel-Menü"""
    # Prüfe welche Spiel-Option gewählt wurde
    if wahl == "1":
        print("Neues Spiel wird gestartet...")
    elif wahl == "2":
        print("Schnelles Spiel wird gestartet...")
    elif wahl == "3":
        print("Spiel wird geladen...")
    elif wahl == "4":
        print("Spiel-Editor wird geöffnet...")
    elif wahl == "5":
        print("Tutorial wird gestartet...")
    elif wahl == "6":
        # Zurück zum Hauptmenü (keine weitere Aktion nötig)
        return
    else:
        # Zeige Fehlermeldung bei ungültiger Eingabe
        print("Ungültige Auswahl.")

def starte_menu():
    """Hauptfunktion: Startet das Menü-System"""
    # Starte eine Endlos-Schleife für das Menü
    while True:
        # Zeige das Hauptmenü
        zeige_hauptmenu()
        # Hole die Benutzer-Eingabe
        benutzer_wahl = hole_benutzer_eingabe()
        # Verarbeite die Wahl und prüfe ob weitergemacht werden soll
        weiter = verarbeite_hauptmenu_wahl(benutzer_wahl)
        # Beende die Schleife wenn der Benutzer "Beenden" gewählt hat
        if not weiter:
            break

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    # Starte das Menü-System
    starte_menu()

# "Das Leben ist wie ein Videospiel - manchmal verliert man, aber man kann immer ein neues Spiel starten." - Unbekannt