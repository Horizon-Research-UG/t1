# Importiere benötigte Module für die Bild-Anzeige
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import log

# Protokolliere den Aufruf dieser Bild-Datei
log.log_call()

def zeige_dorf_bild_terminal():
    """Öffnet das Dorf-Bild im Standard-Bildbetrachter"""
    # Definiere den Pfad zur Bilddatei
    bild_pfad = "das dorf.jpg"
    
    # Prüfe ob die Bilddatei existiert
    if os.path.exists(bild_pfad):
        # Öffne das Bild mit dem Standard-Programm
        os.startfile(bild_pfad)
        print("Das Dorf-Bild wird geöffnet...")
    else:
        # Zeige Fehlermeldung wenn Bild nicht gefunden
        print("Fehler: Das Dorf-Bild wurde nicht gefunden!")

class DorfBildGUI:
    """GUI-Klasse für die Dorf-Bild-Darstellung mit klickbaren Buttons"""
    
    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        # Setze den Fenster-Titel
        self.root.title("NeuroGames - Das Dorf")
        # Erstelle die GUI-Elemente
        self.erstelle_gui()
    
    def erstelle_gui(self):
        """Erstellt alle GUI-Elemente für das Dorf-Bild"""
        # Erstelle den Titel
        titel = tk.Label(self.root, text="🏘️ DAS DORF 🏘️", 
                        font=("Arial", 16, "bold"))
        titel.pack(pady=10)
        
        # Erstelle Frame für das Bild und die Buttons
        haupt_frame = tk.Frame(self.root)
        haupt_frame.pack(pady=10)
        
        # Versuche das Bild zu laden und anzuzeigen
        try:
            # Lade das Bild
            bild = Image.open("das dorf.jpg")
            # Skaliere das Bild auf eine angemessene Größe
            bild = bild.resize((600, 400), Image.Resampling.LANCZOS)
            # Konvertiere für tkinter
            self.foto = ImageTk.PhotoImage(bild)
            
            # Erstelle Frame für Bild mit Buttons
            bild_frame = tk.Frame(haupt_frame)
            bild_frame.pack()
            
            # Links-Button
            links_button = tk.Button(bild_frame, text="◀ LINKS", 
                                   command=self.klick_links,
                                   bg="lightblue", fg="black",
                                   font=("Arial", 12, "bold"),
                                   width=8, height=2)
            links_button.pack(side=tk.LEFT, padx=10)
            
            # Erstelle Label für das Bild
            bild_label = tk.Label(bild_frame, image=self.foto)
            bild_label.pack(side=tk.LEFT)
            
            # Rechts-Button
            rechts_button = tk.Button(bild_frame, text="RECHTS ▶", 
                                    command=self.klick_rechts,
                                    bg="lightgreen", fg="black", 
                                    font=("Arial", 12, "bold"),
                                    width=8, height=2)
            rechts_button.pack(side=tk.RIGHT, padx=10)
            
            # Setze Fenster-Größe basierend auf Bildgröße
            self.root.geometry("800x500")
        except Exception as e:
            # Zeige Fehlermeldung wenn Bild nicht geladen werden kann
            error_label = tk.Label(haupt_frame, text=f"Fehler beim Laden des Bildes:\n{str(e)}", 
                                 fg="red", font=("Arial", 12))
            error_label.pack(pady=20)
            self.root.geometry("400x200")
        
        # Erstelle Button-Frame für Aktionen
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Erstelle Aktions-Buttons
        tk.Button(button_frame, text="🔍 Bild vergrößern", 
                 command=self.vergroessere_bild, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="💾 Bild-Info", 
                 command=self.zeige_bild_info, width=15).pack(side=tk.LEFT, padx=5)
        
        # Erstelle Zurück-Button
        tk.Button(self.root, text="Zurück zum Hauptmenü", 
                 command=self.schliesse_fenster, bg="red", fg="white").pack(pady=10)
    
    def klick_links(self):
        """Aktion wenn Links-Button geklickt wird"""
        # Zeige eine Nachricht für Links-Klick
        messagebox.showinfo("Links-Button", 
                           "🏃‍♂️ Sie gehen nach LINKS!\n\n" +
                           "Sie entdecken:\n" +
                           "• Ein geheimnisvolles Portal\n" +
                           "• Einen alten Pfad im Wald\n" +
                           "• Glitzernde Kristalle am Boden")
        print("Spieler klickte LINKS - Portal entdeckt!")
    
    def klick_rechts(self):
        """Aktion wenn Rechts-Button geklickt wird"""
        # Zeige eine Nachricht für Rechts-Klick
        messagebox.showinfo("Rechts-Button", 
                           "🏃‍♀️ Sie gehen nach RECHTS!\n\n" +
                           "Sie finden:\n" +
                           "• Einen lebhaften Marktplatz\n" +
                           "• Freundliche Dorfbewohner\n" +
                           "• Einen Händler mit seltenen Waren")
        print("Spieler klickte RECHTS - Marktplatz erreicht!")
    
    def vergroessere_bild(self):
        """Öffnet das Originalbild im Standard-Bildbetrachter"""
        zeige_dorf_bild_terminal()
    
    def zeige_bild_info(self):
        """Zeigt Informationen über das Bild"""
        try:
            # Lade das Bild für Info-Abfrage
            bild = Image.open("das dorf.jpg")
            info_text = f"Bildgröße: {bild.size[0]} x {bild.size[1]} Pixel\n"
            info_text += f"Format: {bild.format}\n"
            info_text += f"Modus: {bild.mode}"
            messagebox.showinfo("Bild-Information", info_text)
        except Exception as e:
            messagebox.showerror("Fehler", f"Konnte Bild-Info nicht laden:\n{str(e)}")
    
    def schliesse_fenster(self):
        """Schließt das GUI-Fenster"""
        self.root.destroy()
    
    def starte(self):
        """Startet die GUI-Hauptschleife"""
        self.root.mainloop()

def starte_dorf_bild_gui():
    """Hauptfunktion: Startet das Dorf-Bild als GUI"""
    # Erstelle und starte die Dorf-Bild-GUI
    try:
        dorf_bild_gui = DorfBildGUI()
        dorf_bild_gui.starte()
    except Exception as e:
        print(f"Fehler beim Starten der GUI: {str(e)}")
        # Fallback: Öffne Bild im Standard-Programm
        zeige_dorf_bild_terminal()

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    starte_dorf_bild_gui()

# "Ein Bild sagt mehr als tausend Worte." - Konfuzius