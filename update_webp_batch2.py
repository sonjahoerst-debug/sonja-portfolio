#!/usr/bin/env python3
"""
Ersetzt weitere Bilder durch WebP mit Picture-Element Fallback
"""

import re
import os

# Mapping: Original -> WebP
WEBP_MAPPINGS = {
    # Neue Batch
    'astern_projekt.png': 'astern_projekt.webp',
    'astern.png': 'astern.webp',
    'blechtrommel_plakat.png': 'blechtrommel_plakat.webp',
    'brücke_zug_illu.png': 'brücke_zug_illu.webp',
    'Fashion-Illustration-red.png': 'Fashion-Illustration-red.webp',
    'fashionsketch_illustartion.jpeg': 'fashionsketch_illustartion.webp',
    'hamburg_illustration.jpeg': 'hamburg_illustration.webp',
    'hamburg_wasser_sonja.jpeg': 'hamburg_wasser_sonja.webp',
    'hamburg_wasser.jpeg': 'hamburg_wasser.webp',
    'hamburgwasser.jpeg': 'hamburgwasser.webp',
    'herz_plakat.png': 'herz_plakat.webp',
    'IMG_1174.jpeg': 'IMG_1174.webp',
    'juri_sonja_portarit.jpeg': 'juri_sonja_portarit.webp',
    'karte_illu_rot.png': 'karte_illu_rot.webp',
    'katze_plakat.png': 'katze_plakat.webp',
    'mockup_nasch_macbook.png': 'mockup_nasch_macbook.webp',
    'mockup_nasch_macbook1.png': 'mockup_nasch_macbook1.webp',
    'packaging_back.jpg': 'packaging_back.webp',
    'packaging_gallery.jpg': 'packaging_gallery.webp',
    'plakat_einheit.png': 'plakat_einheit.webp',
    'plakat_hamburg.png': 'plakat_hamburg.webp',
    'plakat_klima.png': 'plakat_klima.webp',
    'portarit_illustration.jpeg': 'portarit_illustration.webp',
    'projekt_swiss.jpeg': 'projekt_swiss.webp',
    'sara_blumen.jpg': 'sara_blumen.webp',
    'schweiz_projekt.jpeg': 'schweiz_projekt.webp',
    'sonja_portrait_illustration.jpeg': 'sonja_portrait_illustration.webp',
    'sonnencreme_projekt.jpg': 'sonnencreme_projekt.webp',
    'sonnenmilch_claim.jpg': 'sonnenmilch_claim.webp',
    'webdesin.jpeg': 'webdesin.webp',
    'website_nasch_projekt.jpeg': 'website_nasch_projekt.webp',
    'wednesday_plakat.png': 'wednesday_plakat.webp',
    'wolf_plakat.png': 'wolf_plakat.webp',
    'zug_rot.jpeg': 'zug_rot.webp',
}

def replace_with_picture(html_content):
    """Ersetzt <img> durch <picture> mit WebP + Fallback"""
    
    for original, webp in WEBP_MAPPINGS.items():
        # Escape special characters
        original_escaped = re.escape(original)
        
        # Pattern für <img src="assets/images/DATEI" ...>
        pattern = r'<img\s+src="assets/images/' + original_escaped + r'"([^>]*)>'
        
        def replacer(match):
            attributes = match.group(1)
            return f'''<picture>
                <source srcset="assets/images_webp/{webp}" type="image/webp">
                <img src="assets/images/{original}"{attributes}>
            </picture>'''
        
        html_content = re.sub(pattern, replacer, html_content)
    
    return html_content

def process_file(filepath):
    """Verarbeitet eine HTML-Datei"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = replace_with_picture(content)
        
        if content != updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            
            # Zähle Ersetzungen
            count = sum(1 for orig in WEBP_MAPPINGS.keys() if orig in content)
            print(f"✅ {filepath}: {count} Bilder auf WebP aktualisiert")
            return True
        else:
            print(f"⏭️  {filepath}: Keine Änderungen")
            return False
            
    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return False

def main():
    files = [
        'index.html', 'about.html', 'portrait.html',
        'project.html', 'project1.html', 'project3.html',
        'project4.html', 'project5.html', 'project6.html',
        'project7.html', 'project8.html'
    ]
    
    print("🖼️  WebP Konvertierung Batch 2\n")
    
    count = 0
    for f in files:
        if os.path.exists(f):
            if process_file(f):
                count += 1
    
    print(f"\n✨ {count} Dateien aktualisiert")
    print(f"📊 {len(WEBP_MAPPINGS)} neue WebP-Bilder mit Fallback eingebaut")

if __name__ == '__main__':
    main()
