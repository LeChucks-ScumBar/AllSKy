#!/usr/bin/env python3
import gps
import time
from datetime import datetime
from pathlib import Path

# Ausgabe-Datei
outfile3 = "/home/raspberry/allsky/gps_coords.txt"
outfile2 = "/home/raspberry/allsky/config/overlay/extra/gps_coords.txt"
outfile = "/home/raspberry/allsky/config/overlay/extra/gps_coords.json"
# Verbindung zu gpsd
session = gps.gps(mode=gps.WATCH_ENABLE)

lat = None
lon = None

# max. 10 Sekunden warten, bis wir Koordinaten bekommen
timeout = time.time() + 10
while time.time() < timeout:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                lat = report.lat
                lon = report.lon
                break
    except KeyError:
        pass
    except StopIteration:
        break

# schreiben, wenn vorhanden
#if lat is not None and lon is not None:
if ((lat > 0) and (lat is not None))  and ((lon > 0) and (lon is not None)):
    with open(outfile, "w") as f:
        f.write(f"{{\n    \"AG_GPS\": \"Lat: {lat}  Lon: {lon}\"\n}}")
    with open(outfile2, "w") as f:
        f.write(f"AG_GPS2=Lat: {lat}  Lon: {lon}")
    with open(outfile3, "w") as f:
        f.write(f"Lat: {lat}  Lon: {lon}")
    print(f"{{\n\"AG_GPS3\": \"Lat: {lat}  Lon: {lon}\"\n}}")
   
    #Speichern in image path
    ##################    

    #datum Ordner
    date_str = datetime.now().strftime("%Y%m%d")
    #Datum Uhrzeit für eintrag
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #Pfad vorbereiten
    base_path = Path("~/allsky//images").expanduser()
    target_dir = base_path / date_str
    target_dir.mkdir(parents=True, exist_ok=True)

    file_path = target_dir / "gps_log.txt"
    print(f"\nPath: {file_path}")
    with open(file_path, "a") as f:
        f.write(f"{timestamp} - Lat: {lat} -  Lon: {lon}\n")

