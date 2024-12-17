import json
import time
from datetime import datetime
# from lora import send_lora_message  # Hvis du ikke vil bruge LoRa, kan du kommentere denne import
from qr_code import scan_qr_code_live
from speech_recognition import recognize_from_microphone
from health_data import extract_health_data, PATTERNS
from system_info import get_wifi_strength, get_ip_address, get_temperature
import uuid

RASPBERRY_ID = str(uuid.uuid4())[:8]  # Forkort UUID til 8 tegn for at spare plads

def main():
    qr_code_data = scan_qr_code_live()
    if qr_code_data:
        recognized_speech = recognize_from_microphone()
        if recognized_speech:
            health_data = extract_health_data(recognized_speech)
            if health_data:
                message_data = {
                    "id": RASPBERRY_ID,
                    "ts": int(time.time()),  # Tidsstempel som UNIX-tid for at spare plads
                    "qr": qr_code_data,
                    "hd": health_data,
                    "ws": get_wifi_strength(),
                    "ip": get_ip_address(),
                    "tmp": get_temperature()
                }
                # Fjern None-værdier for at spare plads
                message_data = {k: v for k, v in message_data.items() if v is not None}
                json_message = json.dumps(message_data, separators=(',', ':'))  # Komprimer JSON

                # Kommenter eller fjern denne linje for at deaktivere LoRa-delen
                # send_lora_message(json_message)  # Denne linje sender beskeden via LoRa
            else:
                print("Ingen sundhedsdata fundet.")
        else:
            print("Ingen tale genkendt.")
    else:
        print("Ingen gyldig QR-kode fundet.")

if __name__ == "__main__":
    main()
