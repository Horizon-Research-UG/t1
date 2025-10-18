# Importiere benötigte Module für GitHub Pages Integration
import os
import webbrowser
import log

# Protokolliere den Aufruf dieser GitHub-Pages-Datei
log.log_call()

def erstelle_github_anleitung():
    """Detaillierte Anleitung für GitHub Pages"""
    print("=" * 80)
    print("🐙 GITHUB PAGES - DAUERHAFT KOSTENLOSE WEBSITE")
    print("=" * 80)
    
    print("📋 SCHRITT-FÜR-SCHRITT ANLEITUNG:")
    print()
    
    print("1️⃣ GITHUB-KONTO ERSTELLEN:")
    print("   • Gehen Sie zu: https://github.com")
    print("   • Klicken Sie auf 'Sign up'")
    print("   • Wählen Sie einen Benutzernamen (z.B. 'IhrName2024')")
    print("   • Bestätigen Sie Ihre E-Mail-Adresse")
    print()
    
    print("2️⃣ NEUES REPOSITORY ERSTELLEN:")
    print("   • Klicken Sie auf 'New repository' (grüner Button)")
    print("   • Repository Name: 'neurogames-dorf'")
    print("   • ✅ Haken bei 'Public'")
    print("   • ✅ Haken bei 'Add a README file'")
    print("   • Klicken Sie 'Create repository'")
    print()
    
    print("3️⃣ DATEIEN HOCHLADEN:")
    print("   • Klicken Sie 'Add file' → 'Upload files'")
    print("   • Ziehen Sie diese Dateien hinein:")
    print("     ✅ spiel_online.html")
    print("     ✅ das dorf.jpg")
    print("   • Schreiben Sie unten: 'NeuroGames Spiel hinzugefügt'")
    print("   • Klicken Sie 'Commit changes'")
    print()
    
    print("4️⃣ GITHUB PAGES AKTIVIEREN:")
    print("   • Klicken Sie auf 'Settings' (oben rechts)")
    print("   • Scrollen Sie runter zu 'Pages' (linke Seite)")
    print("   • Bei 'Source': Wählen Sie 'Deploy from a branch'")
    print("   • Bei 'Branch': Wählen Sie 'main'")
    print("   • Klicken Sie 'Save'")
    print()
    
    print("5️⃣ IHRE WEBSITE IST ONLINE:")
    print("   • Nach 1-2 Minuten ist Ihre Website verfügbar unter:")
    print("     https://IHR-BENUTZERNAME.github.io/neurogames-dorf/spiel_online.html")
    print("   • Diese URL funktioniert von überall auf der Welt!")
    print()
    
    print("✅ VORTEILE VON GITHUB PAGES:")
    print("   🆓 Komplett kostenlos")
    print("   🔒 Automatisches HTTPS")
    print("   🌍 Weltweit erreichbar")
    print("   ⚡ Sehr schnell")
    print("   📱 Mobile-optimiert")
    print("   🔄 Automatische Updates")
    print()
    
    print("💡 BEISPIEL-URLs:")
    print("   https://maxmustermann.github.io/neurogames-dorf/spiel_online.html")
    print("   https://spieleentwickler.github.io/neurogames-dorf/spiel_online.html")
    print("   https://IHR-NAME.github.io/neurogames-dorf/spiel_online.html")
    print()
    
    print("🎮 SO TEILEN SIE IHR SPIEL:")
    print("   'Spielt mein Spiel: https://IHR-NAME.github.io/neurogames-dorf/spiel_online.html'")
    print("   Funktioniert auf jedem Gerät, überall auf der Welt!")
    print()
    
    print("=" * 80)

def oeffne_github():
    """Öffnet GitHub in Browser"""
    print("🐙 GitHub wird geöffnet...")
    webbrowser.open("https://github.com")
    print("✅ GitHub geöffnet! Folgen Sie der Anleitung oben.")

def erstelle_readme_datei():
    """Erstellt eine README.md Datei für GitHub"""
    readme_inhalt = """# 🎮 NeuroGames - Das Dorf

Ein interaktives Browser-Spiel, das von überall gespielt werden kann!

## 🌐 Jetzt spielen
[🎮 **Spiel starten** 🎮](./spiel_online.html)

## 📱 Features
- ✅ Funktioniert auf allen Geräten (Handy, Tablet, PC)
- ✅ Keine Installation erforderlich
- ✅ Interaktive Buttons
- ✅ Schöne Grafiken
- ✅ Von überall erreichbar

## 🎯 Wie man spielt
1. Klicken Sie auf den Link oben
2. Wählen Sie "Dorf besuchen"
3. Klicken Sie auf LINKS oder RECHTS für Abenteuer!

## 🛠️ Technik
- HTML5 + CSS3 + JavaScript
- Responsive Design
- Optimiert für alle Browser

---
Erstellt with ❤️ von NeuroGames
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_inhalt)
    
    print("✅ README.md Datei erstellt!")
    print("📁 Diese Datei können Sie auch auf GitHub hochladen")

def zeige_alternative_hosting():
    """Zeigt weitere kostenlose Hosting-Alternativen"""
    print("=" * 80)
    print("🌐 WEITERE KOSTENLOSE HOSTING-OPTIONEN")
    print("=" * 80)
    
    print("🥇 NETLIFY (Drag & Drop - Super einfach):")
    print("   • Gehen Sie zu: https://app.netlify.com/drop")
    print("   • Ziehen Sie Ihre Dateien einfach auf die Seite")
    print("   • Sofort online verfügbar!")
    print("   • Bekommen eine URL wie: https://abc123.netlify.app")
    print()
    
    print("🥈 VERCEL (Professionell):")
    print("   • Gehen Sie zu: https://vercel.com")
    print("   • Kostenloser Account")
    print("   • GitHub-Integration möglich")
    print("   • Sehr schnell und zuverlässig")
    print()
    
    print("🥉 FIREBASE HOSTING:")
    print("   • Google Firebase Console")
    print("   • Kostenloser Plan verfügbar")
    print("   • Sehr gute Performance")
    print("   • Eigene Domain möglich")
    print()
    
    print("🏆 IHRE EIGENE DOMAIN:")
    print("   • Wenn Sie bereits eine Domain haben")
    print("   • Einfach Dateien hochladen")
    print("   • Professionell und dauerhaft")
    print("   • Volle Kontrolle")
    print()
    
    print("⚡ SCHNELLSTE LÖSUNG:")
    print("   1. Netlify Drop: 30 Sekunden bis online")
    print("   2. GitHub Pages: 5 Minuten bis online") 
    print("   3. Ngrok: Sofort online (temporär)")
    print("=" * 80)

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    print("Wählen Sie eine Option:")
    print("1. GitHub Pages Anleitung")
    print("2. GitHub im Browser öffnen")
    print("3. README.md Datei erstellen")
    print("4. Alternative Hosting-Optionen")
    
    wahl = input("Ihre Wahl (1-4): ")
    
    if wahl == "1":
        erstelle_github_anleitung()
    elif wahl == "2":
        oeffne_github()
    elif wahl == "3":
        erstelle_readme_datei()
    elif wahl == "4":
        zeige_alternative_hosting()
    else:
        print("Ungültige Wahl!")

# "Open Source verbindet Entwickler weltweit." - Linus Torvalds