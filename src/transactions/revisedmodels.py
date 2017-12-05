from django.db import models



# Create your models here.
from django.conf import settings


class Quarter(models.Model):
	quarter = models.CharField(max_length=250)

	class Meta:
		ordering = ('quarter',)

	def __str__(self):
		return self.quarter

class CountryFrom(models.Model):
	countryname = models.CharField(max_length=120, choices=settings.COUNTRIES, default="Belgium")
	flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")	
	currency = models.CharField(max_length=120, null=True, blank=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.countryname

class CountryTo(models.Model):
	countryname = models.CharField(max_length=120, choices=settings.COUNTRIES, default="Belgium")
	flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")	
	currency = models.CharField(max_length=120, null=True, blank=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.countryname

class Amount(models.Model):
	amount = models.CharField(max_length=120, null=True, blank=True)

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.amount

class Record(models.Model):	
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
		return self.firm


class Transaction(models.Model):
	quarter = models.ForeignKey(Quarter)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)	
	country_from = models.ForeignKey(CountryFrom, related_name="countryfrom", on_delete=models.CASCADE)
	# country_from_flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")	
	# country_from_currency = models.CharField(max_length=120, null=True, blank=True)
	country_to = models.ForeignKey(CountryTo, related_name="countryto", on_delete=models.CASCADE)
	# country_to_flag = models.CharField(max_length=120, choices=settings.FLAGS, default="assets/flags/Belgium.png")	
	# country_to_currency = models.CharField(max_length=120, null=True, blank=True)
	amount1 = models.ForeignKey(Amount, related_name="amount_1")
	record1 = models.ForeignKey(Record, related_name="record_1", on_delete=models.CASCADE)
	amount2 = models.ForeignKey(Amount, related_name="amount_2")
	record2 = models.ForeignKey(Record, related_name="record_2", on_delete=models.CASCADE)
	


	#country_from = models.ForeignKey(Country, related_name='countryfrom')
	#country_from_flag = models.ImageField(upload_to="images/countryfromflags/")
	#country_to = models.ForeignKey(Country, related_name='countryto')
	#country_to_flag = models.ImageField(upload_to="images/countrytoflags/")
	#product_availability_icon = models.CharField(max_length=250, null=True, blank=True)
	#product_availability_icon = models.ImageField(upload_to="images/productavailabilityicons/")
	#transfer_speed_icon = models.CharField(max_length=250, null=True, blank=True)
	#transfer_speed_icon = models.ImageField(upload_to="images/transferspeedicons/")
	#network_coverage_icon = models.CharField(max_length=250, null=True, blank=True)
	#network_coverage_icon = models.ImageField(upload_to="networkcoverageicons/")	
	

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.country_from.countryname + " to " + self.country_to.countryname + " | " +self.quarter.quarter
		return settings.COUNTRIES[self.country_from][1] + " to " +settings.COUNTRIES[self.country_to][1] + " | " + self.quarter.quarter