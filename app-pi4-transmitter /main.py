import json
import time
from datetime import datetime
from lora import send_lora_message
from qr_code import scan_qr_code_live
from speech_recognition import recognize_from_microphone
from health_data import extract_health_data, PATTERNS
from system_info import get_wifi_strength, get_ip_address, get_temperature
import uuid

RASPBERRY_ID = str(uuid.uuid4())[:8]


def main():
    qr_code_data = scan_qr_code_live()
    if qr_code_data:
        recognized_speech = recognize_from_microphone()
        if recognized_speech:
            health_data = extract_health_data(recognized_speech)
            if health_data:
                message_data = {
                    "id": RASPBERRY_ID,
                    "ts": int(time.time()),
                    "qr": qr_code_data,
                    "hd": health_data,
                    "ws": get_wifi_strength(),
                    "ip": get_ip_address(),
                    "tmp": get_temperature()
                }
                message_data = {
                    k: v for k, v in message_data.items() if v is not None
                }
                json_message = json.dumps(message_data, separators=(',', ':'))
                send_lora_message(json_message)
                print("Besked sendt via LoRa:", json_message)
            else:
                print("Ingen sundhedsdata fundet.")
        else:
            print("Ingen tale genkendt.")
    else:
        print("Ingen gyldig QR-kode fundet.")


if __name__ == "__main__":
    main()
