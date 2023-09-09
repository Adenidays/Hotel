from django.contrib import admin
from hotel_app.models import  BookingApplication, Room, RoomFeature



admin.site.register(BookingApplication)

admin.site.register(Room)
admin.site.register(RoomFeature)
