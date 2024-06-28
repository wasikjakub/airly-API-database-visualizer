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


### Uruchomienie aplikacji

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

