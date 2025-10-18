# Importiere benötigte Module für die einfache Bild-GUI
import os
import tkinter as tk
from tkinter import messagebox
import log

# Protokolliere den Aufruf dieser einfachen Bild-Datei
log.log_call()

class EinfacheDorfBildGUI:
    """Einfache GUI-Klasse ohne PIL-Abhängigkeit"""
    
    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        # Setze den Fenster-Titel
        self.root.title("NeuroGames - Das Dorf (Einfache Version)")
        # Setze Fenster-Größe
        self.root.geometry("700x400")
        # Erstelle die GUI-Elemente
        self.erstelle_gui()
    
    def erstelle_gui(self):
        """Erstellt alle GUI-Elemente ohne Bild-Anzeige"""
        # Erstelle den Titel
        titel = tk.Label(self.root, text="🏘️ DAS DORF 🏘️", 
                        font=("Arial", 20, "bold"))
        titel.pack(pady=20)
        
        # Info-Text statt Bild
        info_text = tk.Label(self.root, 
                           text="Das Dorf-Bild 'das dorf.jpg' ist verfügbar!\n" +
                                "Verwenden Sie die Buttons unten für Aktionen.",
                           font=("Arial", 12),
                           bg="lightyellow",
                           padx=20, pady=20)
        info_text.pack(pady=20)
        
        # Erstelle Frame für die Haupt-Buttons
        haupt_button_frame = tk.Frame(self.root)
        haupt_button_frame.pack(pady=30)
        
        # Links-Button (großer Button)
        links_button = tk.Button(haupt_button_frame, 
                               text="◀ LINKS\nGehe nach Links", 
                               command=self.klick_links,
                               bg="lightblue", fg="black",
                               font=("Arial", 14, "bold"),
                               width=15, height=4)
        links_button.pack(side=tk.LEFT, padx=20)
        
        # Bild-Button (Mitte)
        bild_button = tk.Button(haupt_button_frame, 
                              text="🖼️\nBild öffnen", 
                              command=self.oeffne_bild,
                              bg="yellow", fg="black",
                              font=("Arial", 12, "bold"),
                              width=12, height=4)
        bild_button.pack(side=tk.LEFT, padx=20)
        
        # Rechts-Button (großer Button)
        rechts_button = tk.Button(haupt_button_frame, 
                                text="RECHTS ▶\nGehe nach Rechts", 
                                command=self.klick_rechts,
                                bg="lightgreen", fg="black", 
                                font=("Arial", 14, "bold"),
                                width=15, height=4)
        rechts_button.pack(side=tk.LEFT, padx=20)
        
        # Erstelle Button-Frame für weitere Aktionen
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Weitere Aktions-Buttons
        tk.Button(button_frame, text="📊 Spiel-Status", 
                 command=self.zeige_status, width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="💾 Speichern", 
                 command=self.speichere_spiel, width=12).pack(side=tk.LEFT, padx=5)
        
        # Erstelle Zurück-Button
        tk.Button(self.root, text="Zurück zum Hauptmenü", 
                 command=self.schliesse_fenster, 
                 bg="red", fg="white", 
                 font=("Arial", 10, "bold")).pack(pady=20)
    
    def klick_links(self):
        """Aktion wenn Links-Button geklickt wird"""
        # Zeige eine Nachricht für Links-Klick
        messagebox.showinfo("Links-Abenteuer", 
                           "🏃‍♂️ Sie gehen nach LINKS!\n\n" +
                           "🌟 Sie entdecken:\n" +
                           "• Ein geheimnisvolles Portal ✨\n" +
                           "• Einen alten Pfad im Wald 🌲\n" +
                           "• Glitzernde Kristalle am Boden 💎\n\n" +
                           "Was möchten Sie tun?")
        print("🎮 Spieler klickte LINKS - Portal entdeckt!")
    
    def klick_rechts(self):
        """Aktion wenn Rechts-Button geklickt wird"""
        # Zeige eine Nachricht für Rechts-Klick
        messagebox.showinfo("Rechts-Abenteuer", 
                           "🏃‍♀️ Sie gehen nach RECHTS!\n\n" +
                           "🏪 Sie finden:\n" +
                           "• Einen lebhaften Marktplatz 🛒\n" +
                           "• Freundliche Dorfbewohner 👥\n" +
                           "• Einen Händler mit seltenen Waren 💰\n\n" +
                           "Der Handel beginnt!")
        print("🎮 Spieler klickte RECHTS - Marktplatz erreicht!")
    
    def oeffne_bild(self):
        """Öffnet das Dorf-Bild im Standard-Programm"""
        # Prüfe ob Bilddatei existiert
        if os.path.exists("das dorf.jpg"):
            # Öffne das Bild
            os.startfile("das dorf.jpg")
            messagebox.showinfo("Bild geöffnet", "Das Dorf-Bild wird in Ihrem Standard-Programm geöffnet!")
        else:
            messagebox.showerror("Fehler", "Die Datei 'das dorf.jpg' wurde nicht gefunden!")
    
    def zeige_status(self):
        """Zeigt den aktuellen Spiel-Status"""
        messagebox.showinfo("Spiel-Status", 
                           "🎮 SPIEL-STATUS 🎮\n\n" +
                           "📍 Standort: Dorf-Zentrum\n" +
                           "💰 Gold: 100 Münzen\n" +
                           "❤️ Gesundheit: 100%\n" +
                           "🎒 Inventar: 3/10 Gegenstände\n" +
                           "🏆 Level: 1")
    
    def speichere_spiel(self):
        """Speichert den aktuellen Spielstand"""
        messagebox.showinfo("Speichern", 
                           "💾 Spiel wurde erfolgreich gespeichert!\n\n" +
                           "Speicherort: Dorf-Zentrum\n" +
                           "Zeitpunkt: Jetzt")
        print("🎮 Spielstand gespeichert!")
    
    def schliesse_fenster(self):
        """Schließt das GUI-Fenster"""
        self.root.destroy()
    
    def starte(self):
        """Startet die GUI-Hauptschleife"""
        self.root.mainloop()

def starte_einfache_dorf_gui():
    """Hauptfunktion: Startet die einfache Dorf-GUI"""
    # Erstelle und starte die einfache Dorf-GUI
    dorf_gui = EinfacheDorfBildGUI()
    dorf_gui.starte()

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    starte_einfache_dorf_gui()

# "Einfachheit ist die höchste Stufe der Vollendung." - Leonardo da Vinci