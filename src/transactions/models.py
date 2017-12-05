from django.db import models

# Create your models here.
from django.conf import settings
# from mongoengine import *

# from smaapi.settings import DBNAME

# connect(DBNAME)


class Quarter(models.Model):
	quarter = models.CharField(max_length=250)

	class Meta:
		ordering = ('quarter',)

	def __str__(self):
		return self.quarter

# class Country(models.Model):
# 	countryname = models.CharField(max_length=120, choices=settings.COUNTRIES, default="Belgium")
# 	flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")
# 	currency = models.CharField(max_length=250, null=True, blank=True)	

# 	class Meta:
# 		ordering = ('countryname',)

# 	def __str__(self):
# 		return self.countryname

class Corridor(models.Model):
	country_from = models.CharField(max_length=120, choices=settings.COUNTRIES, default="Belgium")	
	country_from_flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")
	country_from_currency = models.CharField(max_length=250, null=True, blank=True)	
	country_to = models.CharField(max_length=120, choices=settings.COUNTRIES, default="Belgium")
	country_to_flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")
	country_to_currency = models.CharField(max_length=250, null=True, blank=True)	
	
	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.country_from + " to " + self.country_to

# class Rate(models.Model):
# 	rate = models.CharField(max_length=250, null=True, blank=True)

# 	class Meta:
# 		ordering = ('id',)

# 	def __str__(self):
# 		return self.rate

# class Firm(models.Model):	
# 	firm = models.CharField(max_length=250, null=True, blank=True)		

# 	class Meta:
# 		ordering = ('id',)

# 	def __str__(self):
# 		return self.firm


class Transaction(models.Model):
	quarter = models.ForeignKey(Quarter)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)	
	# country_from = models.ForeignKey(Country, related_name="countryfrom", on_delete=models.CASCADE)	
	# country_to = models.ForeignKey(Country, related_name="countryto", on_delete=models.CASCADE)	
	corridor = models.ForeignKey(Corridor, related_name='corridorname', on_delete=models.CASCADE)
	rate = models.CharField(max_length=250, null=True, blank=True)
	firm = models.CharField(max_length=250, null=True, blank=True)	
	fee = models.CharField(max_length=250, null=True, blank=True)
	ExchangeRateMargin = models.CharField(max_length=250, null=True, blank=True)
	TotalCostPercent = models.CharField(max_length=250, null=True, blank=True)
	TotalCostEur = models.CharField(max_length=250, null=True, blank=True)
	AmountReceived = models.CharField(max_length=250, null=True, blank=True)	
	product_availability = models.CharField(max_length=120, choices=settings.PRODUCT_AVAILABILITY_DEFINITION, default="Branch")
	product_availability_icon = models.CharField(max_length=120, choices=settings.PRODUCT_AVAILABILITY_ICON, default="assets/icons/productavailability/bank_account.png")	
	transfer_speed_definition = models.CharField(max_length=120, choices=settings.TRANSFER_SPEED_DEFINITION, default="Two days")
	transfer_speed_icon = models.CharField(max_length=120, choices=settings.TRANSFER_SPEED_ICON, default="assets/icons/transferspeed/2_days.png")	
	network_coverage_definition = models.CharField(max_length=120, choices=settings.NETWORK_COVERAGE_DEFINITION, default="Main city")
	network_coverage_icon = models.CharField(max_length=120, choices=settings.NETWORK_COVERAGE_ICON, default="assets/icons/network/main_city.png")

		

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.corridor.country_from + " to " + self.corridor.country_to + " | " +self.quarter.quarter + " | " + self.firm
		# return self.country_from.countryname + " to " + self.country_to.countryname + " | " +self.quarter.quarter + " | " + self.firm.firm
		#return settings.COUNTRIES[self.country_from][1] + " to " +settings.COUNTRIES[self.country_to][1] + " | " + self.quarter.quarter