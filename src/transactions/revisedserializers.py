from rest_framework import serializers
from transactions.models import Quarter, Transaction, Record, CountryFrom, CountryTo, Amount

class QuarterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quarter 
		fields =(
			'quarter',
			)
	

class AmountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Amount 
		fields = (
			'amount',
			)
	

class CountryFromSerializer(serializers.ModelSerializer):	
	class Meta:
		model = CountryFrom 
		fields = (
			'countryname',
			'flag' ,
			'currency'
		)
	

class CountryToSerializer(serializers.ModelSerializer):	
	class Meta:
		model = CountryTo 
		fields = (
			'countryname',
			'flag' ,
			'currency'
			)
	

class RecordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Record 
		fields = (
			'firm',
			'product_availability',
			'fee',
			'ExchangeRateMargin',
			'TotalCostPercent',
			'TotalCostEur',
			'AmountReceived',
			'product_availability_icon',
			'transfer_speed_icon',
			'network_coverage_icon',
			'transfer_speed_definition',
			'network_coverage_definition'
			)
		

class TransactionSerializer(serializers.ModelSerializer):
	#country_from = serializers.Field(source='country_from.countryname')
	quarter = QuarterSerializer()
	amount1 = AmountSerializer()
	amount2 = AmountSerializer()
	country_from = CountryFromSerializer()
	country_to = CountryToSerializer()
	record1 = RecordSerializer()
	record2 = RecordSerializer()
	class Meta:
		model = Transaction
		fields = (
				'pk',
				'quarter',
				'timestamp',
				'country_from',
				'country_to',
				'amount1',	
				'record1',
				'amount2',	
				'record2'							
			)



    

   
