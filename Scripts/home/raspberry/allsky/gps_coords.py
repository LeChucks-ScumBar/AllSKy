#!/usr/bin/env python3
import gps
import time

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
if lat > 0  and lon > 0:
    with open(outfile, "w") as f:
        f.write(f"{{\n\"AS_GPS\": \"Lat: {lat}  Lon: {lon}\"\n}}")
    with open(outfile2, "w") as f:
        f.write(f"{{\n\"AS_GPS2\" : \"Lat: {lat}  Lon: {lon}\"\n}}")
    with open(outfile3, "w") as f:
        f.write(f"{{\n\"AS_GPS3\": \"Lat: {lat}  Lon: {lon}\"\n}}")
