from picamera2 import Picamera2
import cv2
import numpy as np

# Kamera starten
picam2 = Picamera2()
picam2.start()

while True:
    # Frame aufnehmen
    frame = picam2.capture_array()

    # Graustufen für Fokusberechnung
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    focus = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Fokuswert auf Bild einblenden
    cv2.putText(frame, f"Focus: {focus:.1f}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Bild anzeigen
    cv2.imshow("Focus Assist", frame)

    # 'q' zum Beenden
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
