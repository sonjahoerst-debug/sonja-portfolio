# WebP Konvertierungs-Anleitung für Sonja's Portfolio

## 🎯 Ziel
Alle 117 Bilder (JPG, JPEG, PNG) zu WebP konvertieren für bessere Performance

---

## Option 1: Automatische Konvertierung mit Homebrew (Empfohlen)

### Schritt 1: WebP Tools installieren
```bash
# Falls Homebrew nicht installiert ist:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# WebP Tools installieren:
brew install webp
```

### Schritt 2: Bilder konvertieren
```bash
cd "/Volumes/Sonja Hörst/sonja_portfolio_website/assets/images"

# Alle JPG/JPEG Dateien konvertieren
for file in *.{jpg,jpeg,JPG,JPEG}; do
  [ -f "$file" ] || continue
  [ "${file:0:2}" = "._" ] && continue
  filename="${file%.*}"
  if [ ! -f "${filename}.webp" ]; then
    cwebp -q 85 "$file" -o "${filename}.webp"
    echo "✅ $file → ${filename}.webp"
  fi
done

# Alle PNG Dateien konvertieren
for file in *.{png,PNG}; do
  [ -f "$file" ] || continue
  [ "${file:0:2}" = "._" ] && continue
  filename="${file%.*}"
  if [ ! -f "${filename}.webp" ]; then
    cwebp -q 90 -lossless "$file" -o "${filename}.webp"
    echo "✅ $file → ${filename}.webp"
  fi
done
```

---

## Option 2: Online-Konvertierung (Ohne Installation)

### Websites für Batch-Konvertierung:
1. **CloudConvert** - https://cloudconvert.com/png-to-webp
   - Bis zu 25 Dateien gleichzeitig
   - Kostenlos

2. **Convertio** - https://convertio.co/de/jpg-webp/
   - Mehrere Dateien gleichzeitig
   - Kostenlos bis 100MB

### Vorgehen:
1. Lade alle Bilder aus `assets/images/` hoch
2. Konvertiere zu WebP (Qualität: 85%)
3. Lade konvertierte WebP-Dateien herunter
4. Ersetze Originale in `assets/images/`

---

## Option 3: macOS Automator (Mit Drittanbieter-App)

### Mit ImageOptim + WebP Plugin:
1. ImageOptim installieren: https://imageoptim.com
2. WebP Plugin installieren
3. Bilder per Drag & Drop konvertieren

---

## ✅ Nach der Konvertierung

Ich aktualisiere dann automatisch alle HTML-Dateien:
- Alle `.jpg` → `.webp`
- Alle `.jpeg` → `.webp`  
- Alle `.png` → `.webp`

### Performance-Verbesserung:
- **WebP ist 25-35% kleiner** als JPG/PNG
- **Schnellere Ladezeiten**
- **Bessere Barrierefreiheit** (schnellere Website)
- **Besseres SEO** (Google bevorzugt schnelle Websites)

---

## 📊 Deine Bilder

- **Gesamt:** 117 Bilder
- **JPG/JPEG:** ~40 Bilder
- **PNG:** ~77 Bilder

**Geschätzte Dateigrößen-Reduktion:** 30-40%

---

## 🚀 Welche Option möchtest du?

Sag mir einfach:
- "Option 1" - Ich führe die Homebrew-Installation + Konvertierung aus
- "Option 2" - Du machst es manuell online
- "Option 3" - Du nutzt ImageOptim

Nach der Konvertierung aktualisiere ich alle HTML-Dateien automatisch! ✨
