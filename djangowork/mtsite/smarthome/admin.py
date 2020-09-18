from django.contrib import admin

# Register your models here.

from .models import Airsensorinfo, Gassensorinfo, Motionsensorinfo, Rainsensorinfo, Tempsensorinfo

admin.site.register(Airsensorinfo)
admin.site.register(Gassensorinfo)
admin.site.register(Motionsensorinfo)
admin.site.register(Rainsensorinfo)
admin.site.register(Tempsensorinfo)