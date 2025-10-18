# Importiere benötigte Module für die GUI
import tkinter as tk
from tkinter import messagebox
import log

# Protokolliere den Aufruf dieser GUI-Datei
log.log_call()

class DorfGUI:
    """GUI-Klasse für die Dorf-Darstellung"""
    
    def __init__(self):
        # Erstelle das Hauptfenster
        self.root = tk.Tk()
        # Setze den Fenster-Titel
        self.root.title("NeuroGames - Dorf")
        # Setze die Fenster-Größe
        self.root.geometry("600x500")
        # Erstelle die GUI-Elemente
        self.erstelle_gui()
    
    def erstelle_gui(self):
        """Erstellt alle GUI-Elemente für das Dorf"""
        # Erstelle den Titel
        titel = tk.Label(self.root, text="🏘️ WILLKOMMEN IM DORF 🏘️", 
                        font=("Arial", 16, "bold"))
        titel.pack(pady=10)
        
        # Erstelle das Dorf-Canvas für Grafiken
        self.canvas = tk.Canvas(self.root, width=500, height=300, bg="lightgreen")
        self.canvas.pack(pady=10)
        
        # Zeichne das Dorf
        self.zeichne_dorf()
        
        # Erstelle Button-Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Erstelle Aktions-Buttons
        tk.Button(button_frame, text="🏠 Haus besuchen", 
                 command=self.besuche_haus, width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="⛪ Kirche besuchen", 
                 command=self.besuche_kirche, width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="💧 Brunnen", 
                 command=self.besuche_brunnen, width=15).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="🌾 Feld bearbeiten", 
                 command=self.bearbeite_feld, width=15).grid(row=1, column=1, padx=5, pady=5)
        
        # Erstelle Zurück-Button
        tk.Button(self.root, text="Zurück zum Hauptmenü", 
                 command=self.schliesse_fenster, bg="red", fg="white").pack(pady=10)
    
    def zeichne_dorf(self):
        """Zeichnet das Dorf auf dem Canvas"""
        # Zeichne Himmel-Hintergrund
        self.canvas.create_rectangle(0, 0, 500, 100, fill="lightblue", outline="")
        
        # Zeichne Boden
        self.canvas.create_rectangle(0, 200, 500, 300, fill="brown", outline="")
        
        # Zeichne Häuser
        self.canvas.create_rectangle(50, 150, 100, 200, fill="red", outline="black")
        self.canvas.create_polygon(25, 150, 75, 120, 125, 150, fill="darkred", outline="black")
        
        self.canvas.create_rectangle(400, 150, 450, 200, fill="blue", outline="black")
        self.canvas.create_polygon(375, 150, 425, 120, 475, 150, fill="darkblue", outline="black")
        
        # Zeichne Kirche in der Mitte
        self.canvas.create_rectangle(220, 130, 280, 200, fill="gray", outline="black")
        self.canvas.create_polygon(200, 130, 250, 100, 300, 130, fill="darkgray", outline="black")
        # Kirchturm
        self.canvas.create_rectangle(240, 100, 260, 130, fill="gray", outline="black")
        self.canvas.create_polygon(235, 100, 250, 80, 265, 100, fill="darkgray", outline="black")
        
        # Zeichne Brunnen
        self.canvas.create_oval(230, 220, 270, 260, fill="darkblue", outline="black", width=3)
        
        # Zeichne Bäume
        self.canvas.create_rectangle(150, 180, 160, 200, fill="brown")
        self.canvas.create_oval(140, 160, 170, 190, fill="green")
        
        self.canvas.create_rectangle(340, 180, 350, 200, fill="brown")
        self.canvas.create_oval(330, 160, 360, 190, fill="green")
        
        # Zeichne Felder
        for i in range(5):
            self.canvas.create_rectangle(80 + i*15, 250, 90 + i*15, 290, 
                                       fill="yellow", outline="green")
    
    def besuche_haus(self):
        """Aktion: Haus besuchen"""
        messagebox.showinfo("Haus", "Sie betreten ein gemütliches Haus!\nEin freundlicher Dorfbewohner begrüßt Sie!")
    
    def besuche_kirche(self):
        """Aktion: Kirche besuchen"""
        messagebox.showinfo("Kirche", "Sie betreten die alte Dorfkirche...\nFriedliche Stille umgibt Sie.")
    
    def besuche_brunnen(self):
        """Aktion: Brunnen untersuchen"""
        messagebox.showinfo("Brunnen", "Sie schauen in den tiefen Brunnen...\nDas Wasser ist kristallklar!")
    
    def bearbeite_feld(self):
        """Aktion: Feld bearbeiten"""
        messagebox.showinfo("Feld", "Sie helfen bei der Feldarbeit...\nDie Bauern sind Ihnen dankbar!")
    
    def schliesse_fenster(self):
        """Schließt das GUI-Fenster"""
        self.root.destroy()
    
    def starte(self):
        """Startet die GUI-Hauptschleife"""
        self.root.mainloop()

def starte_dorf_gui():
    """Hauptfunktion: Startet das Dorf als GUI"""
    # Erstelle und starte die Dorf-GUI
    dorf_gui = DorfGUI()
    dorf_gui.starte()

# Wenn dieses Modul direkt ausgeführt wird
if __name__ == "__main__":
    starte_dorf_gui()

# "In der GUI liegt die Zukunft der Benutzerfreundlichkeit." - Unbekannt