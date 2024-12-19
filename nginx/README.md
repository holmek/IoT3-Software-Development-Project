# Nginx SSL Konfiguration

Dette dokument beskriver, hvordan du opretter et selvsigneret SSL-certifikat og konfigurerer Nginx til at bruge det.

## Generering af SSL-certifikat

1. Opret en mappe til at gemme SSL-certifikaterne, hvis den ikke allerede findes:

    ```bash
    sudo mkdir -p /etc/nginx/ssl
    ```

2. Brug OpenSSL til at generere et selvsigneret certifikat og en privat nøgle:

    ```bash
    sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
    ```

    - `-x509`: Generer et selvsigneret certifikat.
    - `-nodes`: Opret certifikatet uden en adgangskode for nøglen.
    - `-days 365`: Gør certifikatet gyldigt i 365 dage.
    - `-newkey rsa:2048`: Generer en ny RSA-nøgle på 2048 bits.
    - `-keyout`: Angiv filen, hvor den private nøgle gemmes.
    - `-out`: Angiv filen, hvor certifikatet gemmes.

3. Følg instruktionerne på skærmen for at indtaste oplysninger som land, organisation og servernavn.

## Nginx Konfiguration

For at konfigurere Nginx til at bruge SSL-certifikatet, skal du opdatere din Nginx-konfiguration som følger:

1. Åbn din Nginx konfigurationsfil:

    ```bash
    sudo nano /etc/nginx/sites-available/default
    ```

2. Tilføj følgende SSL-konfiguration:

    ```nginx
    server {
        listen 443 ssl;
        server_name localhost;

        ssl_certificate /etc/nginx/ssl/nginx.crt;
        ssl_certificate_key /etc/nginx/ssl/nginx.key;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        gzip on;
        gzip_types text/plain text/css application/javascript application/json application/xml application/xml+rss text/javascript;
        gzip_min_length 1000;

        location / {
            root /var/www/webapp-pi0/dist;
            index index.html index.htm;
        }

        location ~* \.(jpg|jpeg|png|gif|css|js|woff|woff2|ttf|eot|svg|ico|otf|json)$ {
            expires 30d;
            add_header Cache-Control "public, no-transform";
        }

        error_page 404 /404.html;
        error_page 500 502 503 504 /50x.html;

        location = /50x.html {
            root /var/www/html;
        }
    }
    ```

    - Sørg for, at stien til dit SSL-certifikat og din private nøgle stemmer overens med de filer, du har genereret.
    - Angiv den ønskede rodmappe for din webapplikation som `/var/www/webapp-pi0/dist`.

## Genstart Nginx

For at anvende ændringerne skal du genstarte Nginx:

```bash
sudo systemctl restart nginx
