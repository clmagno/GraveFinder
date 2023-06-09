from django.contrib import admin
from .models import CustomUser, Lot, Corpse, Reservation
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Lot)
admin.site.register(Corpse)
admin.site.register(Reservation)