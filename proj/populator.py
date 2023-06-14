import os
import django

import proj.settings

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")
django.setup()
from django.contrib.gis.geos import Point
import csv
from app.models import Lot


def insert_from_csv():

    csv_file_path = "datasheet.csv"

    # Read and process the CSV file
    rows = []
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            if any(field.strip() for field in row):
                rows.append(row)

    # Update existing Lot objects with data from CSV
    for row in rows:
        row_block = row[0]
        row_lot = row[1]
        row_capacity = row[2]
        row_ll1 = row[3]
        row_ll2 = row[4]
        row_ll3 = row[5]
        row_ll4 = row[6]
        if row_capacity == "":
            row_capacity = 0
        lot_data = {
            "block_no": row_block,
            "lot_no": row_lot,
            "phase": "",
            "area": "",
            "capacity": row_capacity,
        }

        if row_ll1:
            lot_data["lat_long1"] = Point(*[float(coord) for coord in row_ll1.split(",")])
        else:
            lot_data["lat_long1"] = Point(0, 0)  # Assign a default Point value
        if row_ll2:
            lot_data["lat_long2"] = Point(*[float(coord) for coord in row_ll2.split(",")])
        else:
            lot_data["lat_long2"] = Point(0, 0)  # Assign a default Point value
        if row_ll3:
            lot_data["lat_long3"] = Point(*[float(coord) for coord in row_ll3.split(",")])
        else:
            lot_data["lat_long3"] = Point(0, 0)  # Assign a default Point value
        if row_ll4:
            lot_data["lat_long4"] = Point(*[float(coord) for coord in row_ll4.split(",")])
        else:
            lot_data["lat_long4"] = Point(0, 0)  # Assign a default Point value

        try:
            lot = Lot.objects.get(block_no=row_block, lot_no=row_lot)
            for key, value in lot_data.items():
                setattr(lot, key, value)
            lot.save()
        except Lot.DoesNotExist:
            # Create a new Lot object if it doesn't exist
            lot = Lot.objects.create(**lot_data)

insert_from_csv()