# Importiere benötigte Module für Online-Server
import http.server
import socketserver
import webbrowser
import os
import socket
import log

# Protokolliere den Aufruf dieser Online-Server-Datei
log.log_call()

def starte_online_server():
    """Startet einen Server der von außen erreichbar ist"""
    # Port für den Online-Server
    PORT = 8080
    
    # Wechsle in das Verzeichnis mit der HTML-Datei
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Ermittle alle IP-Adressen
    hostname = socket.gethostname()
    lokale_ip = socket.gethostbyname(hostname)
    
    # HTTP-Server-Handler
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Server auf allen Interfaces starten (0.0.0.0)
        with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
            print("=" * 80)
            print("🌍 NEUROGAMES ONLINE-SERVER (Für externe Zugriffe)")
            print("=" * 80)
            print(f"🖥️  Server läuft auf Port: {PORT}")
            print(f"💻 Computer-Name: {hostname}")
            print()
            
            print("📍 ZUGRIFFS-URLS:")
            print(f"   Lokal:          http://localhost:{PORT}/spiel_online.html")
            print(f"   Netzwerk:       http://{lokale_ip}:{PORT}/spiel_online.html")
            print()
            
            print("🌐 FÜR EXTERNE ZUGRIFFE (Internet):")
            print("   1. Router-Einstellungen öffnen (meist 192.168.1.1)")
            print(f"   2. Port-Forwarding einrichten: Port {PORT} → {lokale_ip}")
            print("   3. Ihre öffentliche IP ermitteln (whatismyipaddress.com)")
            print(f"   4. Zugriff dann über: http://IHRE-ÖFFENTLICHE-IP:{PORT}/spiel_online.html")
            print()
            
            print("🏠 ALTERNATIVE: EIGENE DOMAIN")
            print("   - Laden Sie 'spiel_online.html' und 'das dorf.jpg' auf Ihre Domain hoch")
            print("   - Zugriff dann über: https://ihre-domain.de/spiel_online.html")
            print("   - Vorteil: HTTPS, keine Router-Konfiguration nötig")
            print()
            
            print("🔧 KOSTENLOSE HOSTING-ALTERNATIVEN:")
            print("   • GitHub Pages (github.com)")
            print("   • Netlify (netlify.com)")
            print("   • Vercel (vercel.com)")
            print("   • Firebase Hosting (firebase.google.com)")
            print()
            
            print("🛡️  SICHERHEITSHINWEISE:")
            print("   ⚠️  Port-Forwarding öffnet Ihren Computer für das Internet")
            print("   ✅ Safer: Verwenden Sie professionelles Web-Hosting")
            print("   ✅ Empfohlen: GitHub Pages oder Netlify für statische Seiten")
            print()
            
            print("⏹️  Drücken Sie Ctrl+C um den Server zu beenden")
            print("=" * 80)
            
            # Browser automatisch öffnen
            webbrowser.open(f'http://localhost:{PORT}/spiel_online.html')
            
            # Server starten
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Online-Server wird beendet...")
        print("👋 Auf Wiedersehen!")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} ist bereits belegt!")
            print("💡 Versuchen Sie einen anderen Port oder beenden Sie andere Programme.")
        else:
            print(f"❌ Fehler beim Starten des Online-Servers: {e}")

def zeige_hosting_anleitung():
    """Zeigt Anleitung für kostenloses Web-Hosting"""
    print("=" * 80)
    print("🌐 KOSTENLOSES WEB-HOSTING ANLEITUNG")
    print("=" * 80)
    
    print("1. GITHUB PAGES (Empfohlen - Kostenlos):")
    print("   • Erstellen Sie ein GitHub-Konto")
    print("   • Erstellen Sie ein neues Repository 'neurogames'")
    print("   • Laden Sie 'spiel_online.html' und 'das dorf.jpg' hoch")
    print("   • Aktivieren Sie GitHub Pages in den Einstellungen")
    print("   • Ihre URL: https://IHR-USERNAME.github.io/neurogames/spiel_online.html")
    print()
    
    print("2. NETLIFY (Sehr einfach):")
    print("   • Gehen Sie zu netlify.com")
    print("   • Ziehen Sie Ihre Dateien per Drag & Drop auf die Seite")
    print("   • Automatische URL wird erstellt")
    print("   • Optional: Eigene Domain verbinden")
    print()
    
    print("3. VERCEL (Professionell):")
    print("   • Erstellen Sie ein Vercel-Konto")
    print("   • Verbinden Sie mit GitHub (falls gewünscht)")
    print("   • Automatisches Deployment")
    print("   • Sehr schnell und zuverlässig")
    print()
    
    print("4. IHRE EIGENE DOMAIN:")
    print("   • Laden Sie die Dateien über FTP/cPanel hoch")
    print("   • Ordnerstruktur: /public_html/spiel_online.html")
    print("   • Zugriff: https://ihre-domain.de/spiel_online.html")
    print()
    
    print("✅ VORTEILE VON WEB-HOSTING:")
    print("   • Automatisches HTTPS")
    print("   • Weltweit erreichbar")
    print("   • Keine Router-Konfiguration")
    print("   • Professionell")
    print("   • Meist kostenlos für statische Seiten")
    print("=" * 80)

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    print("Wählen Sie eine Option:")
    print("1. Online-Server starten (Port-Forwarding nötig)")
    print("2. Hosting-Anleitung anzeigen")
    
    wahl = input("Ihre Wahl (1-2): ")
    
    if wahl == "1":
        starte_online_server()
    elif wahl == "2":
        zeige_hosting_anleitung()
    else:
        print("Ungültige Wahl!")

# "Das Internet macht die Welt zu einem globalen Dorf." - Marshall McLuhan