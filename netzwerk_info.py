# Importiere benötigte Module für Netzwerk-Informationen
import socket
import subprocess
import platform
import log

# Protokolliere den Aufruf dieser Netzwerk-Info-Datei
log.log_call()

def zeige_netzwerk_info():
    """Zeigt alle wichtigen Netzwerk-Informationen für das Spiel"""
    print("=" * 70)
    print("🌐 NEUROGAMES - NETZWERK INFORMATIONEN")
    print("=" * 70)
    
    # Lokale IP ermitteln
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lokale_ip = s.getsockname()[0]
        s.close()
    except Exception:
        lokale_ip = "Nicht verfügbar"
    
    # Computer-Name ermitteln
    computer_name = socket.gethostname()
    
    # Betriebssystem ermitteln
    os_info = platform.system() + " " + platform.release()
    
    print(f"🖥️  Computer-Name: {computer_name}")
    print(f"💻 Betriebssystem: {os_info}")
    print(f"📍 Lokale IP-Adresse: {lokale_ip}")
    print()
    
    print("🎮 SPIEL-ZUGRIFF URLs (Port 8000):")
    print(f"   Lokal:    http://localhost:8000/spiel.html")
    print(f"   Netzwerk: http://{lokale_ip}:8000/spiel.html")
    print()
    
    print("📱 FÜR HANDY/TABLET/ANDERE GERÄTE:")
    print("   1. Verbinden Sie das Gerät mit dem gleichen WLAN")
    print("   2. Öffnen Sie den Browser auf dem Gerät")
    print(f"   3. Geben Sie ein: http://{lokale_ip}:8000/spiel.html")
    print("   4. Das Spiel lädt automatisch!")
    print()
    
    print("🔧 PROBLEMLÖSUNG:")
    print("   • Firewall temporär deaktivieren falls Probleme auftreten")
    print("   • Alle Geräte müssen im gleichen WLAN/Netzwerk sein")
    print("   • Bei Problemen versuchen Sie Port 8080 statt 8000")
    print()
    
    print("🛡️  SICHERHEIT:")
    print("   • Server nur im lokalen Netzwerk sichtbar")
    print("   • Keine Daten werden ins Internet übertragen")
    print("   • Automatisch sicher da nur HTML/CSS/JavaScript")
    print()
    
    # Versuche WLAN-Informationen zu zeigen (Windows)
    if platform.system() == "Windows":
        try:
            print("📶 WLAN-INFORMATIONEN:")
            result = subprocess.run(['netsh', 'wlan', 'show', 'profile'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                profiles = [line.strip().split(': ')[1] for line in lines 
                          if 'Profil für alle Benutzer' in line]
                if profiles:
                    print("   Verfügbare WLAN-Netzwerke:")
                    for profile in profiles[:3]:  # Zeige nur die ersten 3
                        print(f"     • {profile}")
                else:
                    print("   Keine WLAN-Profile gefunden")
            else:
                print("   WLAN-Informationen nicht verfügbar")
        except Exception:
            print("   WLAN-Informationen nicht verfügbar")
    print()
    
    print("🚀 ZUM STARTEN:")
    print("   1. Führen Sie 'main.py' aus")
    print("   2. Wählen Sie '3. Browser-Spiel starten'")
    print("   3. Teilen Sie die Netzwerk-URL mit anderen Geräten")
    print()
    
    print("=" * 70)

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    zeige_netzwerk_info()

# "Das Netzwerk verbindet uns alle." - Tim Berners-Lee