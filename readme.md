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

- **Structure Preview:** </br>
</br>

![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/90352b19-7997-42b7-a070-23ae3a8ab034)

![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/20693e73-98e9-4f07-bffc-504982b7073e)

![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/b8f1e856-2f18-40f0-811a-9ea502125c57)

## File Description

- **app.py**: This file sets up the Dash application. It creates a layout that includes a navigation menu and a page container for dashboards. It also styles the navigation buttons and centers them on the page.

- **database.py**: This file sets up the Flask application and connects to a MySQL database. It defines SQLAlchemy models for storing location data, dust measurements, gas measurements, and AQI indicators. It also initializes the database tables.

- **requests.py**: This file handles fetching data from the Airly API. It includes functions to fetch air quality data, store it in the database, and schedule periodic data fetching using BackgroundScheduler.

## Preview

Watch the dashboards live [here](https://youtu.be/IWB6gRvBP4k)

Dashboard 1: </br>
![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/41271725-39cf-43a5-9d91-bd0a59091c94)

Dashboard 2: </br>
![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/2ec22c37-eee2-437b-b536-41ff1d952bdb)

Dashboard 3: </br>
![image](https://github.com/wasikjakub/airly-API-database-visualizer/assets/144064944/ed98a7dd-1507-4d2d-81f0-81f4f85afcc2)

Example usage video: 

## App

To use the application, it is necessary to run two files. Initially, you need to start the database.py file.

```
python database.py
```

Next, start the file responsible for the dashboards app.py.

```
python app.py
```

### Links

[Mapa](https://airly.org/map/pl/) </br>
[Dokumentacja](https://developer.airly.org/en/docs#introduction) </br>
[Requesty](https://developer.airly.org/en/api) </br>

