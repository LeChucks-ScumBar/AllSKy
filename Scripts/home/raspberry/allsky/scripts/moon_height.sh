# Datei: /home/raspberry/allsky/scripts/run_moon_height.sh
#!/bin/bash

# Pfad zum Python-Skript
SCRIPT="/home/raspberry/allsky/scripts/moon_height.py"

# Log-Datei
LOG="/home/raspberry/allsky/logs/moon_height.log"

# Prüfe, ob Internetverbindung besteht
echo "$(date): Prüfe Internetverbindung..." >> "$LOG"

# Teste mit ping auf Google (kann auch auf 8.8.8.8 gehen)
if ping -c 3 8.8.8.8 >/dev/null 2>&1; then
    echo "$(date): Internetverbindung vorhanden. Führe Skript aus..." >> "$LOG"
    # Führe das Python-Skript aus
    /usr/bin/python3 "$SCRIPT" >> "$LOG" 2>&1
else
    echo "$(date): Keine Internetverbindung. Skript nicht ausgeführt." >> "$LOG"
fi
