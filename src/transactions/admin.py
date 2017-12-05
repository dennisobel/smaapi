from django.contrib import admin
# from .models import Quarter, Transaction, Record, CountryFrom, CountryTo, Amount
from .models import Quarter, Transaction, Corridor
# Register your models here.
admin.site.register(Quarter)
admin.site.register(Transaction)
# admin.site.register(Firm)
admin.site.register(Corridor)
# admin.site.register(Country)

