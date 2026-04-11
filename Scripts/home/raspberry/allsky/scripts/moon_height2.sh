#!/bin/bash

# Log-Datei
LOG="/home/raspberry/allsky/logs/autoupdate_stations_moon.log"

# Funktion: Prüfe Internetverbindung
check_internet() {
    if ping -c 3 8.8.8.8 >/dev/null 2>&1; then
        return 0  # Internet da
    else
        return 1  # Kein Internet
    fi
}

# Log-Eintrag
echo "$(date): --- Neuer Cron-Run ---" >> "$LOG"

# 1. Lade stations.txt herunter (nur bei Internet)
echo "$(date): Lade stations.txt herunter..." >> "$LOG"
if check_internet; then
    wget -q http://celestrak.org/NORAD/elements/stations.txt -O /home/raspberry/allsky/data/stations.txt >> "$LOG" 2>&1
    if [ $? -eq 0 ]; then
        echo "$(date): stations.txt erfolgreich heruntergeladen." >> "$LOG"
    else
        echo "$(date): Fehler beim Herunterladen von stations.txt." >> "$LOG"
    fi
else
    echo "$(date): Kein Internet. stations.txt nicht heruntergeladen." >> "$LOG"
fi

# 2. Führe moon_height.sh aus (bereits mit Internet-Check)
echo "$(date): Führe moon_height.sh aus..." >> "$LOG"
if check_internet; then
    /home/raspberry/allsky/scripts/moon_height.sh >> "$LOG" 2>&1
    echo "$(date): moon_height.sh erfolgreich ausgeführt." >> "$LOG"
else
    echo "$(date): Kein Internet. moon_height.sh nicht ausgeführt." >> "$LOG"
fi

echo "$(date): --- Ende des Runs ---" >> "$LOG"
