# Grave Finder App

The Grave Finder App is a web application developed using Python, Django, Postgres, GDAL, OpenStreetMap, Leaflet.js, HTML, and CSS. It allows users to view a map with overlays of lots, which they can click on and reserve.

## Features

- View a map with overlays of lots
- Click on available lots to reserve them
- Differentiate between available lots (green) and occupied lots (red)
- Input information for reservations
- Dashboard displaying cards representing each block of lots with the number of available and reserved lots

## Technologies Used

- Python
- Django
- Postgres
- GDAL
- OpenStreetMap
- Leaflet.js
- HTML
- CSS
- sb-admin2 Bootstrap

## Configuration and Setup

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/clmagno/GraveFinder.git
   ```

2. Set up Python:

   - Download and install Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Make sure to add Python to your system's PATH during the installation process.

3. Install Conda:

   - Download and install Conda from the official website: [https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

4. Create and activate a new virtual environment:

   ```
   conda create -n grave-finder-env python=3.9
   conda activate grave-finder-env
   ```

5. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

6. Set up PostgreSQL:

   - Download and install PostgreSQL from the official website: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
   - During the installation, set a username and password for the PostgreSQL database.

7. Configure the database:

   - Update the database settings in the `settings.py` file located in the `grave_finder` directory to match your PostgreSQL database configuration:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your-database-name',
             'USER': 'your-username',
             'PASSWORD': 'your-password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

8. Set up GDAL:

   - Download the GDAL library for your operating system and install it.
   - Update the `GDAL_LIBRARY_PATH` in the `settings.py` file with the path to the GDAL library.

9. Run database migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

10. Start the development server:

    ```
    python manage.py runserver
    ```

11. Access the Grave Finder App in your web browser at `http://localhost:8000`.

## Usage

1. Dashboard:
   - The dashboard displays cards representing each block of lots.
   - Each card shows the number of available and reserved lots for that block.

2. Maps Page:
   - The maps page displays a map with overlays of lots.
   - Available lots are colored green, while occupied lots are colored red.
   - Click on a green lot to be redirected to the reservation page.

3. Reservation Page:
   - On the reservation page, input the required information for the reservation.
   - After submitting the information, you will be redirected back to the dashboard.

## License

The Grave Finder App is open-source and released under the [MIT License](LICENSE).

 Feel free to modify and use the code according to your needs.

## Acknowledgements

The Grave Finder App is built using various open-source technologies and libraries. We would like to acknowledge the developers and contributors of the following projects:

- Python: [https://www.python.org/](https://www.python.org/)
- Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Postgres: [https://www.postgresql.org/](https://www.postgresql.org/)
- GDAL: [https://gdal.org/](https://gdal.org/)
- OpenStreetMap: [https://www.openstreetmap.org/](https://www.openstreetmap.org/)
- Leaflet.js: [https://leafletjs.com/](https://leafletjs.com/)
- sb-admin2 Bootstrap: [https://startbootstrap.com/theme/sb-admin-2](https://startbootstrap.com/theme/sb-admin-2)
