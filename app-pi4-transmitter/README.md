## Opsætning af app-pi4-transmitter

1. Klon dette repository til din Raspberry Pi:
   ```bash
   git clone https://github.com/holmek/IoT3-Software-Development-Project.git
   cd IoT3-Software-Development-Project
   cd app-pi4-transmitter
   cd src
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python main.py
