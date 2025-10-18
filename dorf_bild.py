# Importiere benötigte Module für die Dorf-GUI
import os
import tkinter as tk
from tkinter import messagebox
try:
    from PIL import Image, ImageTk
    PIL_VERFÜGBAR = True
except ImportError:
    PIL_VERFÜGBAR = False
import log

# Protokolliere den Aufruf dieser Dorf-Datei
log.log_call()

class DorfGUI:
    """GUI-Klasse für das Dorf mit direkter Bild-Anzeige"""
    
    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        # Setze den Fenster-Titel
        self.root.title("NeuroGames - Das Dorf")
        # Variable für das Bild
        self.foto = None
        # Erstelle die GUI-Elemente
        self.erstelle_gui()
    
    def erstelle_gui(self):
        """Erstellt alle GUI-Elemente für das Dorf mit Bild"""
        # Erstelle den Titel
        titel = tk.Label(self.root, text="🏘️ DAS DORF 🏘️", 
                        font=("Arial", 16, "bold"))
        titel.pack(pady=10)
        
        # Lade und zeige das Bild
        bild_frame = tk.Frame(self.root)
        bild_frame.pack(pady=10)
        
        # Versuche das Bild zu laden
        if self.lade_bild():
            # Erstelle Frame für Bild mit Buttons
            haupt_frame = tk.Frame(bild_frame)
            haupt_frame.pack()
            
            # Links-Button
            links_button = tk.Button(haupt_frame, 
                                   text="◀ LINKS", 
                                   command=self.klick_links,
                                   bg="lightblue", fg="black",
                                   font=("Arial", 12, "bold"),
                                   width=10, height=3)
            links_button.pack(side=tk.LEFT, padx=10, pady=10)
            
            # Bild in der Mitte
            if self.foto:
                bild_label = tk.Label(haupt_frame, image=self.foto, bd=2, relief="solid")
                bild_label.pack(side=tk.LEFT, padx=10)
            
            # Rechts-Button
            rechts_button = tk.Button(haupt_frame, 
                                    text="RECHTS ▶", 
                                    command=self.klick_rechts,
                                    bg="lightgreen", fg="black", 
                                    font=("Arial", 12, "bold"),
                                    width=10, height=3)
            rechts_button.pack(side=tk.RIGHT, padx=10, pady=10)
            
            # Setze Fenster-Größe basierend auf Bildgröße
            self.root.geometry("900x600")
        else:
            # Fallback wenn Bild nicht geladen werden kann
            error_label = tk.Label(bild_frame, 
                                 text="❌ Bild 'das dorf.jpg' konnte nicht geladen werden!\n" +
                                      "Bitte prüfen Sie, ob die Datei existiert.",
                                 fg="red", font=("Arial", 12))
            error_label.pack(pady=20)
            
            # Buttons ohne Bild
            button_frame = tk.Frame(bild_frame)
            button_frame.pack(pady=20)
            
            tk.Button(button_frame, text="◀ LINKS", command=self.klick_links,
                     bg="lightblue", width=15, height=2).pack(side=tk.LEFT, padx=20)
            tk.Button(button_frame, text="RECHTS ▶", command=self.klick_rechts,
                     bg="lightgreen", width=15, height=2).pack(side=tk.RIGHT, padx=20)
            
            self.root.geometry("500x300")
        
        # Info-Text
        info_label = tk.Label(self.root, 
                            text="Klicken Sie auf LINKS oder RECHTS für Abenteuer!",
                            font=("Arial", 10), fg="darkblue")
        info_label.pack(pady=5)
        
        # Erstelle Zurück-Button
        tk.Button(self.root, text="Zurück zum Hauptmenü", 
                 command=self.schliesse_fenster, 
                 bg="red", fg="white", 
                 font=("Arial", 10, "bold")).pack(pady=10)
    
    def lade_bild(self):
        """Lädt das Dorf-Bild für die Anzeige"""
        bild_pfad = "das dorf.jpg"
        
        # Prüfe ob Datei existiert
        if not os.path.exists(bild_pfad):
            print(f"❌ Bild nicht gefunden: {bild_pfad}")
            return False
        
        try:
            if PIL_VERFÜGBAR:
                # Verwende PIL für bessere Bildbearbeitung
                bild = Image.open(bild_pfad)
                # Skaliere das Bild auf angemessene Größe
                bild = bild.resize((500, 350), Image.Resampling.LANCZOS)
                # Konvertiere für tkinter
                self.foto = ImageTk.PhotoImage(bild)
                print("✅ Bild mit PIL geladen")
                return True
            else:
                # Fallback: Verwende tkinter PhotoImage (funktioniert nur mit .gif, .pgm, .ppm)
                # Für .jpg müssen wir PIL verwenden oder das Bild konvertieren
                print("⚠️ PIL nicht verfügbar - kann .jpg nicht direkt laden")
                return False
                
        except Exception as e:
            print(f"❌ Fehler beim Laden des Bildes: {str(e)}")
            return False
    
    def klick_links(self):
        """Aktion wenn Links-Button geklickt wird"""
        # Zeige eine Nachricht für Links-Klick
        messagebox.showinfo("Links-Abenteuer", 
                           "🏃‍♂️ Sie gehen nach LINKS!\n\n" +
                           "🌟 Sie entdecken:\n" +
                           "• Ein geheimnisvolles Portal ✨\n" +
                           "• Einen alten Pfad im Wald 🌲\n" +
                           "• Glitzernde Kristalle am Boden 💎")
        print("🎮 Spieler klickte LINKS - Portal entdeckt!")
    
    def klick_rechts(self):
        """Aktion wenn Rechts-Button geklickt wird"""
        # Zeige eine Nachricht für Rechts-Klick
        messagebox.showinfo("Rechts-Abenteuer", 
                           "🏃‍♀️ Sie gehen nach RECHTS!\n\n" +
                           "🏪 Sie finden:\n" +
                           "• Einen lebhaften Marktplatz 🛒\n" +
                           "• Freundliche Dorfbewohner 👥\n" +
                           "• Einen Händler mit seltenen Waren 💰")
        print("🎮 Spieler klickte RECHTS - Marktplatz erreicht!")
    
    def schliesse_fenster(self):
        """Schließt das GUI-Fenster"""
        self.root.destroy()
    
    def starte(self):
        """Startet die GUI-Hauptschleife"""
        self.root.mainloop()

def starte_dorf_gui():
    """Hauptfunktion: Startet die Dorf-GUI"""
    # Erstelle und starte die Dorf-GUI
    dorf_gui = DorfGUI()
    dorf_gui.starte()

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    starte_dorf_gui()

# "Einfachheit ist die höchste Stufe der Vollendung." - Leonardo da Vinci