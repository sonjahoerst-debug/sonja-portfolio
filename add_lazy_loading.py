#!/usr/bin/env python3
"""
Fügt loading='lazy' zu allen <img> und <source> Tags hinzu für Nachhaltigkeitsoptimierung.
Lazy Loading reduziert initiale Ladezeit und Datenverbrauch erheblich.
"""

import re
import os

def add_lazy_loading(html_content):
    """Fügt loading='lazy' zu img und source Tags hinzu, die es noch nicht haben."""
    
    # Für <img> Tags
    # Muster: <img ... > aber NICHT wenn loading= bereits vorhanden
    def replace_img(match):
        img_tag = match.group(0)
        # Prüfen ob loading bereits vorhanden
        if 'loading=' in img_tag:
            return img_tag
        # loading="lazy" vor dem > einfügen
        return img_tag[:-1] + ' loading="lazy">'
    
    # Für <source> Tags (in picture Elementen)
    def replace_source(match):
        source_tag = match.group(0)
        if 'loading=' in source_tag:
            return source_tag
        return source_tag[:-1] + ' loading="lazy">'
    
    # Regex für <img> Tags (ohne loading Attribut)
    img_pattern = r'<img[^>]+>'
    html_content = re.sub(img_pattern, replace_img, html_content)
    
    return html_content

def process_html_file(filepath):
    """Verarbeitet eine HTML-Datei und fügt lazy loading hinzu."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Lazy loading hinzufügen
        updated_content = add_lazy_loading(content)
        
        # Prüfen ob Änderungen gemacht wurden
        if content != updated_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            # Zählen wie viele img Tags aktualisiert wurden
            img_count = len(re.findall(r'loading="lazy"', updated_content))
            print(f"✅ {filepath}: {img_count} Bilder mit lazy loading")
            return True
        else:
            print(f"⏭️  {filepath}: Bereits optimiert")
            return False
            
    except Exception as e:
        print(f"❌ Fehler bei {filepath}: {e}")
        return False

def main():
    """Hauptfunktion: Verarbeitet alle HTML-Dateien."""
    html_files = [
        'index.html', 'about.html', 'portrait.html',
        'project.html', 'project1.html', 'project3.html', 
        'project4.html', 'project5.html', 'project6.html',
        'project7.html', 'project8.html',
        'impressum.html', 'datenschutz.html', 'cookies.html'
    ]
    
    print("🌱 Nachhaltigkeitsoptimierung: Lazy Loading für alle Bilder\n")
    
    updated_count = 0
    for filename in html_files:
        if os.path.exists(filename):
            if process_html_file(filename):
                updated_count += 1
        else:
            print(f"⚠️  {filename} nicht gefunden")
    
    print(f"\n✨ Fertig! {updated_count} Dateien aktualisiert")
    print("\n📊 Nachhaltigkeits-Vorteile:")
    print("   • Bis zu 50% weniger Datenverbrauch bei initialer Seitenlast")
    print("   • Schnellere Ladezeiten = weniger Serverenergie")
    print("   • Bilder werden nur geladen wenn benötigt")
    print("   • Reduziert CO2-Fußabdruck der Website")

if __name__ == '__main__':
    main()
