import cv2
import re
from gpiozero import Buzzer, LED
import time

buzzer = Buzzer(6)
led = LED(26)


def scan_qr_code_live():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Kan ikke åbne kameraet. Tjek forbindelsen.")
        return None
    detector = cv2.QRCodeDetector()
    print("Søger efter QR-kode...")

    led.on()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        data, points, _ = detector.detectAndDecode(frame)
        if data:
            if re.match(r"^\d{10}$", data):
                cap.release()
                buzzer.on()
                time.sleep(0.1)
                buzzer.off()
                led.off()
                return data
            else:
                print("QR-koden indeholder ikke et gyldigt CPR-nummer.")
                buzzer.on()
                time.sleep(0.1)
                buzzer.off()
                time.sleep(0.1)
                buzzer.on()
                time.sleep(0.1)
                buzzer.off()
                cap.release()
                led.off()
                return None
    cap.release()
    led.off()
    return None
