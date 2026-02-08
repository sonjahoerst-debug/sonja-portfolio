#!/usr/bin/env python3
"""
Script zum Aktualisieren der Video-Tags in HTML-Dateien.
Fügt WebM-Format als erste Quelle hinzu (bessere Kompression).
"""

import re
import os

# Mapping: HTML-Datei → Liste der Video-Pfade die aktualisiert werden sollen
video_mappings = {
    'project1.html': [
        ('assets/videos/heroimage_zug.mp4', 'assets/videos/heroimage_zug.webm'),
        ('assets/videos/schweiz_video.mp4', 'assets/videos/schweiz_video.webm'),
    ],
    'project3.html': [
        ('assets/videos/webapp_paula.mp4', 'assets/videos/webapp_paula.webm'),
    ],
    'project5.html': [
        ('assets/videos/nasch_website.mp4', 'assets/videos/nasch_website.webm'),
    ],
}

def update_video_tags(html_file, video_paths):
    """Aktualisiert Video-Tags in einer HTML-Datei."""
    
    if not os.path.exists(html_file):
        print(f"❌ Datei nicht gefunden: {html_file}")
        return False
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changes_made = 0
    
    for mp4_path, webm_path in video_paths:
        # Suche nach der MP4-Source-Zeile
        # Pattern: <source src="assets/videos/VIDEO.mp4" type="video/mp4">
        pattern = rf'(<source src="{re.escape(mp4_path)}" type="video/mp4">)'
        
        # Prüfe ob WebM schon existiert
        if webm_path in content:
            print(f"  ℹ️  WebM bereits vorhanden: {webm_path}")
            continue
        
        # Ersetze mit WebM + MP4
        replacement = f'<source src="{webm_path}" type="video/webm">\n                    <source src="{mp4_path}" type="video/mp4">'
        
        new_content = re.sub(pattern, replacement, content)
        
        if new_content != content:
            content = new_content
            changes_made += 1
            print(f"  ✅ Aktualisiert: {os.path.basename(mp4_path)} → WebM + MP4")
    
    # Speichern nur wenn Änderungen vorgenommen wurden
    if content != original_content:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    """Hauptfunktion."""
    print("🎬 Video-Tag Aktualisierung\n")
    print("=" * 50)
    
    total_files = 0
    total_updates = 0
    
    for html_file, video_paths in video_mappings.items():
        print(f"\n📄 {html_file}")
        
        if update_video_tags(html_file, video_paths):
            total_files += 1
            total_updates += len(video_paths)
    
    print("\n" + "=" * 50)
    print(f"✨ Fertig! {total_files} Dateien aktualisiert")
    print(f"📊 Insgesamt {total_updates} Video-Tags erweitert")
    print("\n💡 Hinweis: Vergiss nicht, die WebM-Dateien zu erstellen!")

if __name__ == "__main__":
    main()
