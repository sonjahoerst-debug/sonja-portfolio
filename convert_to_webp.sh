#!/bin/bash

# WebP Konvertierungs-Skript für Sonja's Portfolio
# Konvertiert alle JPG, JPEG und PNG zu WebP mit guter Qualität

echo "🖼️  WebP Konvertierung gestartet..."
echo "=================================="

# Zähler
converted=0
skipped=0
errors=0

# Gehe zum Bilder-Ordner
cd "/Volumes/Sonja Hörst/sonja_portfolio_website/assets/images"

# Finde alle Bild-Dateien (ohne macOS ._* Dateien)
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) ! -name "._*" | while read file; do
    # Dateiname ohne Erweiterung
    filename="${file%.*}"
    
    # Prüfe ob WebP schon existiert
    if [ -f "${filename}.webp" ]; then
        echo "⏭️  Übersprungen (existiert): ${file}"
        ((skipped++))
    else
        echo "🔄 Konvertiere: ${file}"
        
        # Konvertiere mit sips zu WebP (Qualität 85%)
        if sips -s format webp "${file}" --out "${filename}.webp" > /dev/null 2>&1; then
            echo "✅ Erstellt: ${filename}.webp"
            ((converted++))
        else
            echo "❌ Fehler bei: ${file}"
            ((errors++))
        fi
    fi
done

echo ""
echo "=================================="
echo "✨ Konvertierung abgeschlossen!"
echo "✅ Konvertiert: ${converted} Bilder"
echo "⏭️  Übersprungen: ${skipped} Bilder"
echo "❌ Fehler: ${errors} Bilder"
echo ""
echo "📝 Nächster Schritt: HTML-Dateien aktualisieren"
echo "   (Alle .jpg/.png Referenzen zu .webp ändern)"
