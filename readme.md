## Airly

A project that collects and presents data retrieved from the [Airly](https://airly.org/map/pl/#50.057224,19.933157,i103904) platform.

To connect to the database, it is necessary to use a VPN or be on the AGH network.

## Used Technologies

- **Flask**: backend + SQLAlchemy
- **urllib.request**: API requests
- **BackgroundScheduler**: to execute requests at specified intervals
- **sqlalchemy.orm**: to create sessions and send data to the database
- **Dash**: frontend, creating dashboards

```
pip install -r requirements.txt
```

## Database

We use a MySQL database available from AGH: </br>

[Baza](https://mysql.agh.edu.pl/phpMyAdmin/index.php) </br>

## File Description

app.py: This file sets up the Dash application. It creates a layout that includes a navigation menu and a page container for dashboards. It also styles the navigation buttons and centers them on the page.

database.py: This file sets up the Flask application and connects to a MySQL database. It defines SQLAlchemy models for storing location data, dust measurements, gas measurements, and AQI indicators. It also initializes the database tables.

requests.py: This file handles fetching data from the Airly API. It includes functions to fetch air quality data, store it in the database, and schedule periodic data fetching using BackgroundScheduler.

## Previev

Dashboard 1:

Dashboard 2:

Dashboard 3:

Example usage video: 

## Uruchomienie aplikacji

To use the application, it is necessary to run two files. Initially, you need to start the database.py file.

```
python database.py
```

Next, start the file responsible for the dashboards app.py.

```
python app.py
```

### Linki

[Mapa](https://airly.org/map/pl/) </br>
[Dokumentacja](https://developer.airly.org/en/docs#introduction) </br>
[Requesty](https://developer.airly.org/en/api) </br>

