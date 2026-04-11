from skyfield.api import Topos, load
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import DateFormatter
import os


# Pfad zur GPS-Datei
gps_file = os.path.expanduser("~/allsky/gps_coords.txt")

# GPS-Koordinaten aus Datei laden
def load_gps_coords(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"GPS-Datei nicht gefunden: {file_path}")

    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("Lat:") and "Lon:" in line:
            parts = line.split("Lon:")
            lat_part = parts[0].strip().replace("Lat:", "").strip()
            lon_part = parts[1].strip()
            try:
                latitude = float(lat_part)
                longitude = float(lon_part)
                return latitude, longitude
            except ValueError:
                raise ValueError(f"Ungültige Koordinaten in Datei: {line}")

    raise ValueError("Keine gültigen GPS-Koordinaten in der Datei gefunden.")

# Lade GPS-Koordinaten
try:
    latitude, longitude = load_gps_coords(gps_file)
    print(f"GPS-Koordinaten geladen: Lat={latitude}, Lon={longitude}")
except Exception as e:
    print(f"Fehler beim Laden der GPS-Koordinaten: {e}")
    # Fallback-Werte, falls Datei fehlt
    latitude = 50.88
    longitude = 7.62
    print(f"Fallback-Koordinaten verwendet: {latitude}, {longitude}")

# Standort anpassen
location = Topos(latitude, longitude)

# Lade Mond
ts = load.timescale()
eph = load('de421.bsp')
moon = eph['moon']
earth = eph['earth']

# Zeitpunkte: jede 10 Minuten über Nacht
now = datetime.utcnow()
times = [now + timedelta(minutes=10*i) for i in range(0, 72)]  # 12h

alts = []
for t in times:
    t_ts = ts.utc(t.year, t.month, t.day, t.hour, t.minute)
    alt, az, distance = (earth + location).at(t_ts).observe(moon).apparent().altaz()
    alts.append(alt.degrees)

# Grafik erstellen
plt.figure(figsize=(6, 2), facecolor='black')  # Hintergrund schwarz

# Setze Text- und Linienfarbe auf Weiß
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.alpha'] = 0.3

# Plot mit weißen Linien und Markern
plt.plot(times, alts, color='yellow', marker='o', markersize=3, linewidth=1.5)
plt.fill_between(times, 0, alts, color='yellow', alpha=0.2)

# Titel und Achsenbeschriftung in Weiß
plt.title('Mondhöhe über Nacht', color='white', fontsize=10)
plt.ylabel('Höhe (°)', color='white', fontsize=9)
plt.xlabel('Zeit (HH:MM)', color='white', fontsize=9)

# X-Achse: Formatiere die Zeit als HHMM (z. B. 2230, 2300, 0000)
ax = plt.gca()
ax.xaxis.set_major_formatter(DateFormatter("%H:%M"))  # Format: HHMM
plt.xticks(rotation=0)

# Y-Achse
plt.ylim(0, 90)
plt.tight_layout()

# Optional: Gitter hinzufügen (in leicht grau, damit es nicht zu stark auffällt)
plt.grid(True, which='major', linestyle='--', alpha=0.4)

# Zeige den Plot an
plt.show()


# Speichern für Overlay
plt.savefig('/home/raspberry/allsky/images/moon_height.png', dpi=100)
plt.savefig('/home/raspberry/allsky/config/overlay/images/moon_height.png', dpi=100)
#plt.savefig('/home/raspberry/allsky/config/overlay/images/compass-red.png', dpi=100)
plt.savefig('/home/raspberry/allsky/config/overlay/imagethumbnails/moon_height.png', dpi=100)
#plt.savefig('/home/raspberry/allsky/config/overlay/imagethumbnails/compass-red.png', dpi=10>

