from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CountryList)
admin.site.register(StateList)
admin.site.register(DistrictList)
admin.site.register(CityList)

admin.site.register(Programming)
admin.site.register(Course)