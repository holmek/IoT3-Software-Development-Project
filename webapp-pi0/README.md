
## Opsætning af webapp-pi0

1. Klon dette repository til din Raspberry Pi:
   ```bash
   git clone https://github.com/holmek/IoT3-Software-Development-Project.git
   cd IoT3-Software-Development-Project
   cd webapp-pi0
   cd src
   npm install
   npm run dev
   ```

   Hvis den skal bruges i forbindelse med Nginx eller lignende, så kør:
   ```bash
   npm run build
   ```

2. Gentag processen, hvis du ønsker at klone projektet igen eller arbejde på en ny kopi:
   ```bash
   git clone https://github.com/holmek/IoT3-Software-Development-Project.git
   cd IoT3-Software-Development-Project
   cd webapp-pi0
   cd src
   npm install
   npm run build
   ```
