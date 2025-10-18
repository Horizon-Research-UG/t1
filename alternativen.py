# Importiere benötigte Module für Serveo (SSH-Tunnel ohne Installation)
import subprocess
import os
import time
import threading
import http.server
import socketserver
import webbrowser
import log

# Protokolliere den Aufruf dieser Serveo-Datei
log.log_call()

def starte_serveo_tunnel():
    """Startet Serveo-Tunnel - keine Installation nötig!"""
    PORT = 8000
    
    print("=" * 70)
    print("🌍 SERVEO-TUNNEL (Keine Installation nötig!)")
    print("=" * 70)
    
    try:
        # Starte lokalen Webserver
        print("🖥️  Lokaler Webserver wird gestartet...")
        
        def server_starten():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f"✅ Server läuft auf Port {PORT}")
                httpd.serve_forever()
        
        # Server in separatem Thread starten
        server_thread = threading.Thread(target=server_starten, daemon=True)
        server_thread.start()
        
        time.sleep(2)  # Kurz warten
        
        print("🌐 Serveo-Tunnel wird erstellt...")
        print("⏳ Bitte warten...")
        
        # Erstelle Serveo-Tunnel (funktioniert über SSH)
        serveo_command = f'ssh -R 80:localhost:{PORT} serveo.net'
        
        print()
        print("🎉 SERVEO-ANWEISUNGEN:")
        print("=" * 70)
        print("📋 FÜHREN SIE DIESEN BEFEHL IN PowerShell AUS:")
        print(f"   {serveo_command}")
        print()
        print("📝 SCHRITT-FÜR-SCHRITT:")
        print("1. Öffnen Sie eine neue PowerShell")
        print("2. Kopieren Sie den Befehl oben")
        print("3. Fügen Sie ein und drücken Enter")
        print("4. Sie erhalten eine URL like: https://abc123.serveo.net")
        print("5. Teilen Sie: https://abc123.serveo.net/spiel_online.html")
        print()
        print("✅ VORTEILE VON SERVEO:")
        print("   • Keine Installation nötig")
        print("   • Kostenlos")
        print("   • Sofort verfügbar")
        print("   • Von überall erreichbar")
        print()
        print("⏹️  Dieser lokale Server läuft weiter...")
        print("   Drücken Sie Ctrl+C um zu beenden")
        print("=" * 70)
        
        # Server läuft weiter
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Serveo-Server wird beendet...")
        print("👋 Server geschlossen!")
    except Exception as e:
        print(f"❌ Fehler: {e}")

def starte_localtunnel():
    """Alternative: LocalTunnel (auch ohne Installation)"""
    PORT = 8000
    
    print("=" * 70)
    print("🌐 LOCALTUNNEL - ALTERNATIVE LÖSUNG")
    print("=" * 70)
    
    print("📋 ANWEISUNGEN FÜR LOCALTUNNEL:")
    print()
    print("1. Node.js installieren (falls nicht vorhanden):")
    print("   • Gehen Sie zu: https://nodejs.org")
    print("   • Laden Sie die LTS-Version herunter")
    print("   • Installieren Sie Node.js")
    print()
    print("2. LocalTunnel installieren:")
    print("   • Öffnen Sie PowerShell")
    print("   • Führen Sie aus: npm install -g localtunnel")
    print()
    print("3. Tunnel starten:")
    print(f"   • Führen Sie aus: lt --port {PORT}")
    print("   • Sie erhalten eine URL wie: https://abc123.loca.lt")
    print("   • Teilen Sie: https://abc123.loca.lt/spiel_online.html")
    print()
    print("✅ VORTEIL: Sehr stabil und zuverlässig")
    print("=" * 70)

def ngrok_problemlosung():
    """Hilft bei Ngrok-Problemen"""
    print("=" * 70)
    print("🔧 NGROK PROBLEMLÖSUNG")
    print("=" * 70)
    
    print("❌ HÄUFIGE NGROK-PROBLEME UND LÖSUNGEN:")
    print()
    
    print("1️⃣ NGROK.EXE NICHT GEFUNDEN:")
    print("   Problem: 'ngrok.exe' ist nicht im richtigen Ordner")
    print("   Lösung:")
    print("   • Gehen Sie zu: https://ngrok.com/download")
    print("   • Laden Sie ngrok.exe herunter")
    print(f"   • Speichern Sie es hier: {os.getcwd()}")
    print()
    
    print("2️⃣ AUTHTOKEN FEHLT:")
    print("   Problem: 'ERROR: authentication required'")
    print("   Lösung:")
    print("   • Erstellen Sie ein kostenloses Konto auf ngrok.com")
    print("   • Kopieren Sie Ihren Authtoken")
    print("   • PowerShell: .\\ngrok.exe authtoken IHR_TOKEN")
    print()
    
    print("3️⃣ PORT BEREITS BELEGT:")
    print("   Problem: 'bind: address already in use'")
    print("   Lösung:")
    print("   • Ändern Sie den Port in webserver.py von 8000 auf 8080")
    print("   • Oder beenden Sie andere Programme die Port 8000 nutzen")
    print()
    
    print("4️⃣ FIREWALL BLOCKIERT:")
    print("   Problem: Verbindung wird blockiert")
    print("   Lösung:")
    print("   • Windows Firewall temporär deaktivieren")
    print("   • Oder ngrok.exe zur Firewall-Ausnahme hinzufügen")
    print()
    
    print("🆘 SCHNELLE ALTERNATIVE OHNE NGROK:")
    print("   1. Serveo (Option verfügbar im Menü)")
    print("   2. GitHub Pages (dauerhaft kostenlos)")
    print("   3. Netlify Drop (30 Sekunden)")
    print("   4. LocalTunnel (mit Node.js)")
    print()
    print("=" * 70)

def starte_einfachsten_weg():
    """Der absolut einfachste Weg ohne Installation"""
    print("=" * 70)
    print("⚡ DER EINFACHSTE WEG - NETLIFY DROP")
    print("=" * 70)
    
    print("🎯 IN 30 SEKUNDEN ONLINE - GARANTIERT!")
    print()
    print("📋 SO GEHT'S:")
    print("1. Öffnen Sie: https://app.netlify.com/drop")
    print("2. Ziehen Sie diese Dateien in den Browser:")
    print("   • spiel_online.html")
    print("   • das dorf.jpg")
    print("3. FERTIG! Sie bekommen sofort eine URL")
    print("4. Teilen Sie die URL + /spiel_online.html")
    print()
    print("🌍 BEISPIEL-ERGEBNIS:")
    print("   https://wonderful-game-123456.netlify.app/spiel_online.html")
    print()
    print("✅ VORTEILE:")
    print("   • Funktioniert sofort")
    print("   • Keine Installation")
    print("   • Keine Konfiguration")
    print("   • Automatisches HTTPS")
    print("   • Von überall erreichbar")
    print()
    print("🚀 NETLIFY DROP WIRD GEÖFFNET...")
    webbrowser.open("https://app.netlify.com/drop")
    print("✅ Ziehen Sie Ihre Dateien einfach rein!")
    print("=" * 70)

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    print("🔧 NGROK FUNKTIONIERT NICHT? HIER SIND ALTERNATIVEN:")
    print()
    print("1. Serveo-Tunnel starten (ohne Installation)")
    print("2. LocalTunnel-Anleitung") 
    print("3. Ngrok-Problemlösung")
    print("4. Einfachster Weg: Netlify Drop")
    
    wahl = input("Ihre Wahl (1-4): ")
    
    if wahl == "1":
        starte_serveo_tunnel()
    elif wahl == "2":
        starte_localtunnel()
    elif wahl == "3":
        ngrok_problemlosung()
    elif wahl == "4":
        starte_einfachsten_weg()
    else:
        print("Ungültige Wahl!")

# "Wenn ein Weg nicht funktioniert, gibt es immer einen anderen." - Thomas Edison