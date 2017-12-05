from django.contrib import admin
from .models import Quarter, Transaction, Record, CountryFrom, CountryTo, Amount
# Register your models here.
admin.site.register(Quarter)
admin.site.register(Transaction)
admin.site.register(Record)
admin.site.register(CountryFrom)
admin.site.register(CountryTo)
admin.site.register(Amount)
