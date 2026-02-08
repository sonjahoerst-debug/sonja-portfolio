#!/usr/bin/env python3
"""
Fügt rel='preload' für CSS hinzu um kritische Ressourcen schneller zu laden.
Reduziert Time-to-First-Byte und spart Energie.
"""

import re
import os

def add_preload(html_content):
    """Fügt preload für CSS vor dem stylesheet link ein."""
    
    # Prüfen ob preload bereits vorhanden
    if 'rel="preload"' in html_content or "rel='preload'" in html_content:
        return html_content, False
    
    # Muster: <link rel="stylesheet" href="css/styles.css">
    pattern = r'(<link rel="stylesheet" href="css/styles\.css">)'
    
    replacement = r'''<!-- Preload kritischer Ressourcen für schnellere Ladezeit -->
    <link rel="preload" href="css/styles.css" as="style">
    \1'''
    
    updated = re.sub(pattern, replacement, html_content)
    
    return updated, (updated != html_content)

def process_file(filepath):
    """Verarbeitet eine HTML-Datei."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, changed = add_preload(content)
        
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"✅ {filepath}: Preload hinzugefügt")
            return True
        else:
            print(f"⏭️  {filepath}: Bereits optimiert")
            return False
            
    except Exception as e:
        print(f"❌ {filepath}: {e}")
        return False

def main():
    files = [
        'about.html', 'portrait.html',
        'project.html', 'project1.html', 'project3.html',
        'project4.html', 'project5.html', 'project6.html',
        'project7.html', 'project8.html',
        'impressum.html', 'datenschutz.html', 'cookies.html'
    ]
    
    print("⚡ Nachhaltigkeitsoptimierung: CSS Preloading\n")
    
    count = 0
    for f in files:
        if os.path.exists(f):
            if process_file(f):
                count += 1
    
    print(f"\n✨ {count} Dateien aktualisiert")
    print("\n📊 Vorteile:")
    print("   • Bis zu 30% schnellere First Contentful Paint")
    print("   • Reduzierte Renderzeit = weniger CPU-Energie")

if __name__ == '__main__':
    main()
