# Importiere benötigte Module für Ngrok-Integration
import subprocess
import os
import time
import webbrowser
import log

# Protokolliere den Aufruf dieser Ngrok-Datei
log.log_call()

def installiere_ngrok():
    """Anleitung zur Ngrok-Installation"""
    print("=" * 70)
    print("🚀 NGROK INSTALLATION - EINFACHSTER WEG INS INTERNET")
    print("=" * 70)
    print()
    print("📋 SCHRITT-FÜR-SCHRITT ANLEITUNG:")
    print()
    print("1. NGROK HERUNTERLADEN:")
    print("   • Gehen Sie zu: https://ngrok.com")
    print("   • Erstellen Sie ein kostenloses Konto")
    print("   • Laden Sie ngrok.exe herunter")
    print("   • Speichern Sie ngrok.exe in diesem Ordner:")
    print(f"     {os.getcwd()}")
    print()
    print("2. NGROK EINRICHTEN:")
    print("   • Öffnen Sie PowerShell in diesem Ordner")
    print("   • Führen Sie aus: .\\ngrok.exe authtoken IHR_TOKEN")
    print("   • (Token finden Sie in Ihrem ngrok Dashboard)")
    print()
    print("3. AUTOMATISCHER START:")
    print("   • Wählen Sie dann Menüoption '9. Ngrok-Tunnel starten'")
    print("   • Sie erhalten eine öffentliche URL wie:")
    print("     https://abc123.ngrok.io/spiel_online.html")
    print()
    print("✅ VORTEILE VON NGROK:")
    print("   • Funktioniert sofort")
    print("   • Keine Router-Konfiguration")
    print("   • Automatisches HTTPS") 
    print("   • Von überall auf der Welt erreichbar")
    print("   • Kostenlos für den Grundbedarf")
    print()
    print("🌐 BEISPIEL-NUTZUNG:")
    print("   1. Sie starten den Ngrok-Tunnel")
    print("   2. Ngrok zeigt: https://abc123.ngrok.io")
    print("   3. Freunde können von überall zugreifen:")
    print("      https://abc123.ngrok.io/spiel_online.html")
    print()
    print("=" * 70)

def starte_ngrok_tunnel():
    """Startet Ngrok-Tunnel für weltweiten Zugriff"""
    PORT = 8000
    
    # Prüfe ob ngrok.exe existiert
    if not os.path.exists("ngrok.exe"):
        print("❌ ngrok.exe nicht gefunden!")
        print("📋 Bitte installieren Sie ngrok zuerst:")
        installiere_ngrok()
        return
    
    print("=" * 70)
    print("🌍 NGROK-TUNNEL WIRD GESTARTET...")
    print("=" * 70)
    
    try:
        # Starte den lokalen Webserver im Hintergrund
        print("🖥️  Lokaler Webserver wird gestartet...")
        import threading
        import http.server
        import socketserver
        
        def server_starten():
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                httpd.serve_forever()
        
        # Server in separatem Thread starten
        server_thread = threading.Thread(target=server_starten, daemon=True)
        server_thread.start()
        
        time.sleep(2)  # Kurz warten bis Server läuft
        
        print("🌐 Ngrok-Tunnel wird erstellt...")
        print("⏳ Bitte warten...")
        
        # Starte ngrok
        ngrok_process = subprocess.Popen([
            "ngrok.exe", "http", str(PORT)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        print()
        print("🎉 NGROK IST GESTARTET!")
        print("=" * 70)
        print("📋 ANWEISUNGEN:")
        print("1. Öffnen Sie einen neuen Browser-Tab")
        print("2. Gehen Sie zu: http://localhost:4040")
        print("3. Kopieren Sie die 'Forwarding' URL (https://...ngrok.io)")
        print("4. Teilen Sie diese URL + /spiel_online.html mit Freunden:")
        print("   Beispiel: https://abc123.ngrok.io/spiel_online.html")
        print()
        print("🌍 IHRE FREUNDE KÖNNEN JETZT VON ÜBERALL ZUGREIFEN!")
        print("📱 Funktioniert auf Handy, Tablet, PC - weltweit!")
        print()
        print("⏹️  Drücken Sie Ctrl+C um den Tunnel zu beenden")
        print("=" * 70)
        
        # Öffne ngrok Dashboard
        webbrowser.open("http://localhost:4040")
        
        # Warte auf Benutzer-Eingabe
        ngrok_process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Ngrok-Tunnel wird beendet...")
        print("👋 Tunnel geschlossen!")
    except Exception as e:
        print(f"❌ Fehler beim Starten von Ngrok: {e}")
        print("💡 Stellen Sie sicher, dass ngrok.exe installiert ist")

def zeige_internet_anleitung():
    """Zeigt alle Möglichkeiten für Internet-Zugriff"""
    print("=" * 80)
    print("🌍 INTERNET-ZUGRIFF - ALLE MÖGLICHKEITEN")
    print("=" * 80)
    
    print("🥇 EMPFOHLEN: NGROK (Einfachste Lösung)")
    print("   ✅ Kostenlos, sofort verfügbar")
    print("   ✅ Keine Router-Konfiguration nötig")
    print("   ✅ Automatisches HTTPS")
    print("   ✅ Von überall erreichbar")
    print("   📋 Anleitung: Menü → '10. Ngrok installieren'")
    print()
    
    print("🥈 PROFESSIONELL: Eigene Domain/Hosting")
    print("   ✅ Professionell und dauerhaft")
    print("   ✅ Eigene URL (z.B. meinspiel.de)")
    print("   ✅ Keine Zeitbegrenzung")
    print("   📋 Dateien: spiel_online.html + das dorf.jpg hochladen")
    print()
    
    print("🥉 KOSTENLOS: GitHub Pages")
    print("   ✅ Dauerhaft kostenlos")
    print("   ✅ Automatisches HTTPS")
    print("   ✅ URL: ihrusername.github.io/projektname")
    print("   📋 GitHub Konto → Repository → Files hochladen → Pages aktivieren")
    print()
    
    print("🔧 TECHNISCH: Port-Forwarding")
    print("   ⚠️  Router-Konfiguration erforderlich")
    print("   ⚠️  Sicherheitsrisiko")
    print("   ⚠️  Dynamische IP-Probleme")
    print("   📋 Nur für erfahrene Benutzer empfohlen")
    print()
    
    print("🚀 SOFORT-LÖSUNGEN:")
    print("   1. Ngrok: 5 Minuten Setup, sofort weltweit erreichbar")
    print("   2. Netlify: Drag & Drop Ihre Dateien, kostenlose URL")
    print("   3. GitHub Pages: Code hochladen, automatische Website")
    print()
    
    print("💡 TIPP FÜR FREUNDE/FAMILIE:")
    print("   'Hey, spielt mein Spiel: https://abc123.ngrok.io/spiel_online.html'")
    print("   Funktioniert sofort auf jedem Gerät weltweit!")
    print("=" * 80)

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    print("Wählen Sie eine Option:")
    print("1. Ngrok-Tunnel starten")
    print("2. Ngrok-Installation anzeigen")  
    print("3. Alle Internet-Zugriff Möglichkeiten")
    
    wahl = input("Ihre Wahl (1-3): ")
    
    if wahl == "1":
        starte_ngrok_tunnel()
    elif wahl == "2":
        installiere_ngrok()
    elif wahl == "3":
        zeige_internet_anleitung()
    else:
        print("Ungültige Wahl!")

# "Das Internet verbindet Menschen über alle Grenzen hinweg." - Tim Berners-Lee