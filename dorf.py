# Importiere das Log-Modul für die Aufruf-Protokollierung
import log

# Protokolliere den Aufruf dieser Dorf-Datei
log.log_call()

def zeige_dorf_terminal():
    """Zeigt das Dorf als ASCII-Art im Terminal"""
    # Lösche den Bildschirm für bessere Darstellung
    print("\n" * 3)
    # Zeige den Dorf-Titel
    print("=== WILLKOMMEN IM DORF ===")
    print()
    
    # Zeige das Dorf als ASCII-Art
    print("        🌳    🏠    🌳")
    print("    🌾      /🚪\\      🌾")
    print("  🌾🌾     /____\\    🌾🌾")
    print("    🌳   🏠  ⛪  🏠   🌳")
    print("        /🚪\\|⛪|/🚪\\")
    print("       /____\\|__|/____\\")
    print("  🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾🌾")
    print("    🐄    💧    🐄")
    print("  🌾🌾🌾 Brunnen 🌾🌾🌾")
    print()
    
    # Zeige verfügbare Aktionen
    print("=== DORF AKTIONEN ===")
    print("1. Haus besuchen")
    print("2. Kirche besuchen") 
    print("3. Brunnen untersuchen")
    print("4. Feld bearbeiten")
    print("5. Zurück zum Hauptmenü")
    print("=" * 21)

def verarbeite_dorf_wahl(wahl):
    """Verarbeitet die Benutzer-Auswahl im Dorf"""
    # Prüfe welche Dorf-Aktion gewählt wurde
    if wahl == "1":
        print("Sie betreten ein gemütliches Haus...")
        print("Ein freundlicher Dorfbewohner begrüßt Sie!")
    elif wahl == "2":
        print("Sie betreten die alte Dorfkirche...")
        print("Friedliche Stille umgibt Sie.")
    elif wahl == "3":
        print("Sie schauen in den tiefen Brunnen...")
        print("Das Wasser ist kristallklar!")
    elif wahl == "4":
        print("Sie helfen bei der Feldarbeit...")
        print("Die Bauern sind Ihnen dankbar!")
    elif wahl == "5":
        # Zurück zum Hauptmenü
        return False
    else:
        print("Ungültige Auswahl im Dorf.")
    # Warte auf Benutzereingabe bevor weitergemacht wird
    input("Drücken Sie Enter um fortzufahren...")
    return True

def starte_dorf_terminal():
    """Hauptfunktion: Startet das Dorf im Terminal"""
    # Starte Dorf-Schleife
    while True:
        # Zeige das Dorf
        zeige_dorf_terminal()
        # Hole Benutzer-Eingabe
        from menu import hole_benutzer_eingabe
        dorf_wahl = hole_benutzer_eingabe()
        # Verarbeite die Wahl
        weiter = verarbeite_dorf_wahl(dorf_wahl)
        # Prüfe ob zurück zum Hauptmenü
        if not weiter:
            break

# "Ein Dorf ist ein Buch, das man mit den Füßen liest." - Russisches Sprichwort