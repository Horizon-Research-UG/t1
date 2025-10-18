/*
==============================================
WIX INTEGRATION ANLEITUNG - NeuroGames
==============================================

METHODE 1: HTML-EMBED (Empfohlen)
----------------------------------
1. Öffnen Sie Ihren Wix-Editor
2. Klicken Sie auf "+ Hinzufügen" 
3. Wählen Sie "Mehr" → "HTML iframe"
4. Kopieren Sie den unten stehenden Code hinein
5. Passen Sie Breite/Höhe an (empfohlen: 800x600px)

METHODE 2: Externe Verlinkung
-----------------------------
1. Laden Sie spiel_online.html auf ein kostenloses Hosting hoch
2. Erstellen Sie einen Button in Wix
3. Verlinken Sie den Button zur externen URL

METHODE 3: Wix Code (Velo)
-------------------------
1. Aktivieren Sie Wix Code/Velo
2. Erstellen Sie eine neue Seite
3. Fügen Sie den JavaScript-Code hinzu

VORTEILE VON WIX:
✅ Kostenlos möglich
✅ Automatisches HTTPS
✅ Mobile-optimiert
✅ Weltweit erreichbar
✅ Keine technischen Kenntnisse nötig

NACHTEILE:
❌ Eingeschränkte Anpassungsmöglichkeiten
❌ Wix-Branding bei kostenlosen Accounts
❌ Iframe-Größenbeschränkungen
*/

// WIX-KOMPATIBLE VERSION DES SPIELS
// Diese Version ist optimiert für iframe-Einbettung

function erstelleWixSpiel() {
    const wixSpielCode = `
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NeuroGames - Wix Version</title>
    <style>
        body {
            margin: 0;
            padding: 10px;
            font-family: Arial, sans-serif;
            background: linear-gradient(45deg, #667eea, #764ba2);
            min-height: 100vh;
        }
        
        .wix-container {
            background: white;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            max-width: 100%;
            margin: 0 auto;
        }
        
        .wix-title {
            color: #2c3e50;
            font-size: 24px;
            margin-bottom: 20px;
        }
        
        .wix-buttons {
            display: flex;
            gap: 15px;
            justify-content: center;
            flex-wrap: wrap;
            margin: 20px 0;
        }
        
        .wix-button {
            padding: 15px 25px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .wix-left { background: #3498db; color: white; }
        .wix-right { background: #2ecc71; color: white; }
        
        .wix-button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .wix-image {
            max-width: 300px;
            max-height: 200px;
            border-radius: 10px;
            margin: 10px 0;
        }
        
        .wix-info {
            color: #7f8c8d;
            font-size: 14px;
            margin-top: 15px;
        }
        
        @media (max-width: 500px) {
            .wix-buttons { flex-direction: column; align-items: center; }
            .wix-button { width: 200px; margin: 5px 0; }
        }
    </style>
</head>
<body>
    <div class="wix-container">
        <h1 class="wix-title">🏘️ NeuroGames - Das Dorf</h1>
        
        <div class="wix-buttons">
            <button class="wix-button wix-left" onclick="abenteuer('links')">◀ LINKS</button>
            <button class="wix-button wix-right" onclick="abenteuer('rechts')">RECHTS ▶</button>
        </div>
        
        <img src="https://ihre-domain.de/das-dorf.jpg" alt="Das Dorf" class="wix-image" 
             onerror="this.style.display='none'; document.getElementById('fallback').style.display='block';">
        
        <div id="fallback" style="display:none; padding:20px; background:#ecf0f1; border-radius:10px;">
            🏘️ Das Dorf<br><small>Bild wird geladen...</small>
        </div>
        
        <div id="nachricht" style="margin-top:15px; font-weight:bold; color:#2c3e50;"></div>
        
        <div class="wix-info">
            Wix-Version | Von überall erreichbar
        </div>
    </div>
    
    <script>
        function abenteuer(richtung) {
            const nachrichten = {
                links: "🏃‍♂️ Sie gehen nach LINKS!\\n\\n🌟 Sie entdecken ein Portal!",
                rechts: "🏃‍♀️ Sie gehen nach RECHTS!\\n\\n🏪 Sie finden einen Marktplatz!"
            };
            
            document.getElementById('nachricht').innerHTML = 
                nachrichten[richtung].replace(/\\n/g, '<br>');
            
            setTimeout(() => {
                document.getElementById('nachricht').innerHTML = 
                    'Klicken Sie erneut für weitere Abenteuer!';
            }, 3000);
        }
        
        console.log('🎮 NeuroGames Wix-Version geladen!');
    </script>
</body>
</html>`;
    
    return wixSpielCode;
}

// Ausgabe für Copy-Paste in Wix
console.log("Kopieren Sie den folgenden Code für Wix:");
console.log(erstelleWixSpiel());