# Importiere benötigte Module für den Webserver
import http.server
import socketserver
import webbrowser
import os
import socket
import log

# Protokolliere den Aufruf dieser Webserver-Datei
log.log_call()

def hole_lokale_ip():
    """Ermittelt die lokale IP-Adresse des Computers"""
    try:
        # Erstelle eine Verbindung um die lokale IP zu ermitteln
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Verbinde zu Google DNS
        lokale_ip = s.getsockname()[0]
        s.close()
        return lokale_ip
    except Exception:
        return "localhost"

def starte_webserver():
    """Startet einen Netzwerk-Webserver für das Browser-Spiel"""
    # Setze den Port für den Webserver
    PORT = 8000
    # Ermittle die lokale IP-Adresse
    lokale_ip = hole_lokale_ip()
    
    # Wechsle in das Verzeichnis mit der HTML-Datei
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Erstelle den HTTP-Server (0.0.0.0 = alle Netzwerk-Interfaces)
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Starte den Server auf allen Interfaces
        with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
            print("=" * 60)
            print("🌐 NEUROGAMES NETZWERK-SERVER GESTARTET!")
            print("=" * 60)
            print(f"📍 Server läuft auf Port: {PORT}")
            print()
            print("🖥️  LOKAL (Dieser Computer):")
            print(f"   http://localhost:{PORT}/spiel.html")
            print(f"   http://127.0.0.1:{PORT}/spiel.html")
            print()
            print("� NETZWERK (Andere Geräte):")
            print(f"   http://{lokale_ip}:{PORT}/spiel.html")
            print()
            print("🔗 ALLE ZUGRIFFS-URLS:")
            print(f"   - Handy/Tablet: http://{lokale_ip}:{PORT}/spiel.html")
            print(f"   - Laptop:       http://{lokale_ip}:{PORT}/spiel.html")
            print(f"   - PC im Netz:   http://{lokale_ip}:{PORT}/spiel.html")
            print()
            print("📋 ANLEITUNG FÜR ANDERE GERÄTE:")
            print("   1. Stellen Sie sicher, dass alle Geräte im gleichen WLAN sind")
            print("   2. Geben Sie die Netzwerk-URL in den Browser ein")
            print("   3. Das Spiel lädt automatisch!")
            print()
            print("🛡️  SICHERHEIT:")
            print("   - Server nur im lokalen Netzwerk erreichbar")
            print("   - Keine Internet-Verbindung erforderlich")
            print()
            print("⏹️  Drücken Sie Ctrl+C um den Server zu beenden")
            print("=" * 60)
            
            # Öffne automatisch den Browser auf diesem Computer
            webbrowser.open(f'http://localhost:{PORT}/spiel.html')
            
            # Server läuft bis Ctrl+C gedrückt wird
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server wird beendet...")
        print("👋 Auf Wiedersehen!")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} ist bereits belegt!")
            print("💡 Versuchen Sie einen anderen Port oder beenden Sie andere Programme.")
        else:
            print(f"❌ Fehler beim Starten des Servers: {e}")

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    starte_webserver()

# "Das Internet ist für uns alle da." - Tim Berners-Lee