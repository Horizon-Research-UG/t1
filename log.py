# Importiere benötigte Module für Datei-Operationen und Zeit
import os
import datetime
import inspect

# Definiere den Namen der Log-Datei
LOG_FILE = "log.txt"

# Schwarze Brett Variable - universell verwendbar in allen Programmen
Sumcount = 0

def get_current_time():
    """Gibt die aktuelle Zeit als formatierten String zurück"""
    # Hole die aktuelle Zeit
    now = datetime.datetime.now()
    # Formatiere die Zeit als lesbaren String
    return now.strftime("%Y-%m-%d %H:%M:%S")

def get_caller_info():
    """Ermittelt Informationen über das aufrufende Programm"""
    # Hole den aktuellen Aufruf-Stack
    frame = inspect.currentframe()
    # Gehe zwei Ebenen zurück (diese Funktion -> log_call -> aufrufendes Programm)
    caller_frame = frame.f_back.f_back
    # Hole den Dateinamen des aufrufenden Programms
    caller_filename = caller_frame.f_code.co_filename
    # Extrahiere nur den Dateinamen ohne Pfad
    caller_name = os.path.basename(caller_filename)
    # Hole den vollständigen Pfad
    caller_path = os.path.abspath(caller_filename)
    # Gib beide Informationen zurück
    return caller_name, caller_path

def read_call_count():
    """Liest die aktuelle Anzahl der Aufrufe aus der Log-Datei"""
    # Prüfe ob die Log-Datei existiert
    if not os.path.exists(LOG_FILE):
        # Wenn nicht, gib 0 zurück
        return 0
    
    try:
        # Öffne die Log-Datei zum Lesen
        with open(LOG_FILE, 'r', encoding='utf-8') as file:
            # Lese alle Zeilen
            lines = file.readlines()
            # Gib die Anzahl der Zeilen zurück (= Anzahl Aufrufe)
            return len(lines)
    except:
        # Bei Fehlern gib 0 zurück
        return 0

def write_log_entry(caller_name, caller_path, current_time, call_number):
    """Schreibt einen neuen Eintrag an den ANFANG der Log-Datei"""
    # Erstelle den neuen Log-Eintrag als formatierten String
    new_log_entry = f"Aufruf #{call_number}: {caller_name} von {caller_path} um {current_time}\n"
    
    # Lese alle existierenden Einträge (falls die Datei existiert)
    existing_entries = ""
    if os.path.exists(LOG_FILE):
        # Öffne die Log-Datei zum Lesen
        with open(LOG_FILE, 'r', encoding='utf-8') as file:
            # Lese alle bisherigen Einträge
            existing_entries = file.read()
    
    # Öffne die Log-Datei zum kompletten Überschreiben
    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        # Schreibe ZUERST den neuen Eintrag (oben)
        file.write(new_log_entry)
        # Dann schreibe alle alten Einträge darunter
        file.write(existing_entries)

def log_call():
    """Hauptfunktion: Protokolliert einen Aufruf dieses Moduls"""
    
    # Hole Informationen über das aufrufende Programm
    caller_name, caller_path = get_caller_info()
    
    # Hole die aktuelle Zeit
    current_time = get_current_time()
    
    # Lese die aktuelle Anzahl der Aufrufe
    current_count = read_call_count()
    
    # Erhöhe die Anzahl um 1 für diesen neuen Aufruf
    new_count = current_count + 1
    
    # Aktualisiere die Schwarze Brett Variable mit der neuen Aufruf-Nummer
    schwarz_brettcount = new_count
    
    # Schreibe den neuen Log-Eintrag
    write_log_entry(caller_name, caller_path, current_time, new_count)
    
    # Gib eine Bestätigung zurück
    print(f"Log-Eintrag #{new_count} erstellt für {caller_name}")

# Wenn dieses Modul direkt ausgeführt wird (nicht importiert)
if __name__ == "__main__":
    # Führe die Log-Funktion aus
    log_call()