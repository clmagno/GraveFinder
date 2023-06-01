import os
import django
import proj.settings
# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'proj.settings')
django.setup()

from app.models import Lot
from django.contrib.gis.geos import Point

def insert_lot(lot,ll1,ll2,ll3,ll4):
    lot = Lot.objects.create(
        block_no='Memory-F1',
        lot_no=lot,
        phase='',
        area='',
        capacity=3,
        lat_long1=Point(ll1),
        lat_long2=Point(ll2),
        lat_long3=Point(ll3),
        lat_long4=Point(ll4),
    )
    print("Lot inserted successfully.")

ll1=14.111401071791715, 121.55021320020109
ll2=14.111371157192366, 121.5502406928427
ll3=14.111402372426372, 121.55027422045443
ll4=14.111430986387134, 121.55024941002175

insert_lot(1,ll1,ll2,ll3,ll4)