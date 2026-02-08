#!/usr/bin/env python3
import os
import re

# Mapping der Dateien (ohne Dateierweiterung) zu ihren WebP-Versionen
file_mappings = {
    # about.html
    'sonja_start.JPG': 'sonja_start.webp',
    
    # project7.html
    'Fashion-Illustration-red.png': 'Fashion-Illustration-red.webp',
    'sara_illustration.jpeg': 'sara_illustration.webp',
    'CEDE5B7D-3F88-49DE-AAAE-FB41FAE51D77_1_105_c.jpeg': 'CEDE5B7D-3F88-49DE-AAAE-FB41FAE51D77_1_105_c.webp',
    'enten_amngeln_illustration.jpeg': 'enten_amngeln_illustration.webp',
    'juri_sonja_portarit.jpeg': 'juri_sonja_portarit.webp',
    'portarit_illustration.jpeg': 'portarit_illustration.webp',
    'portrait_illustartion.jpeg': 'portrait_illustartion.webp',
    
    # project6.html - Plakate
    'plakat_einheit.png': 'plakat_einheit.webp',
    'wednesday_plakat.png': 'wednesday_plakat.webp',
    'plakat_klima.png': 'plakat_klima.webp',
    'pferd_plakat.png': 'pferd_plakat.webp',
    'wolf_plakat.png': 'wolf_plakat.webp',
    'blechtrommel_plakat.png': 'blechtrommel_plakat.webp',
    'plakat_hamburg.png': 'plakat_hamburg.webp',
    'katze_plakat.png': 'katze_plakat.webp',
    'herz_plakat.png': 'herz_plakat.webp',
    
    # project5.html - Nasch
    'Bild_14.jpg': 'Bild_14 (1).webp',
    'mockup_nasch_macbook.png': 'mockup_nasch_macbook.webp',
    'mockup_nasch_macbook1.png': 'mockup_nasch_macbook1.webp',
    
    # project3.html - Paula's Garden
    'blueten_news.jpg': 'blueten_news.webp',
    'mockup_webapp.png': 'mockup_webapp_01.webp',
    'mockup_qiuz_webapp.png': 'mockup_qiuz_webapp.webp',
    'mockup_webapp_01.png': 'mockup_webapp_01.webp',
    
    # project4.html - Sonnenmilch
    'IMG_1174.jpg': 'IMG_1174.webp',
    'sonnenmilch_claim.PNG': 'sonnenmilch_claim.webp',
    
    # project8.html - Hamburg Wasser
    'hamburg_wasser_sonja.jpeg': 'hamburg_wasser_sonja.webp',
    'hamburgwasser.jpg': 'hamburgwasser.webp',
    'hamburg_wasser.JPG': 'hamburg_wasser.webp',
}

# HTML-Dateien zum Durchsuchen
html_files = [
    'about.html',
    'project3.html',
    'project4.html',
    'project5.html',
    'project6.html',
    'project7.html',
    'project8.html',
    'portrait.html'
]

# Arbeitsverzeichnis
base_dir = '/Users/sonjahoerst/Desktop/sonja_portfolio_website'

for html_file in html_files:
    file_path = os.path.join(base_dir, html_file)
    
    if not os.path.exists(file_path):
        print(f"⚠️  Datei nicht gefunden: {html_file}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = 0
    
    # Ersetze alle Pfade
    for old_file, new_file in file_mappings.items():
        old_path = f'assets/images/{old_file}'
        new_path = f'assets/images_webp/{new_file}'
        
        if old_path in content:
            content = content.replace(old_path, new_path)
            changes_made += 1
            print(f"✅ {html_file}: {old_file} → {new_file}")
    
    # Speichere nur wenn Änderungen vorgenommen wurden
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"📝 {html_file}: {changes_made} Bilder ersetzt\n")
    else:
        print(f"➖ {html_file}: Keine Änderungen\n")

print("\n✨ Fertig!")
