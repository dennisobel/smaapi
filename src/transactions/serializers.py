from rest_framework import serializers
from transactions.models import Quarter, Transaction, Corridor 

class CorridorSerializer(serializers.ModelSerializer):
	# country_from = serializers.SlugRelatedField(read_only=True, slug_field='countryname')
	# country_to = serializers.SlugRelatedField(read_only=True, slug_field='countryname')
	# country_from_flag = serializers.SlugRelatedField(read_only=True, slug_field='flag')
	# country_to_flag = serializers.SlugRelatedField(read_only=True, slug_field='flag')
	# corridorname = serializers.StringRelatedField(many=False)
	class Meta:
		model = Corridor 
		fields = (
			'country_from',
			'country_from_flag',
			'country_from_currency',
			'country_to',
			'country_to_flag',
			'country_to_currency',
			)

class QuarterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quarter 
		fields = (
			'id',
			'quarter',
			)

# class CountrySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Country
# 		fields = (
# 			'countryname',
# 			'flag' ,
# 			'currency'
# 		)

# class RateSerializer(serializers.ModelSerializer):
# 	# firm = FirmSerializer()
# 	class Meta:
# 		model = Rate
# 		fields = (
# 			'rate',
# 			)

# class FirmSerializer(serializers.ModelSerializer):
# 	# rate = RateSerializer()
# 	class Meta:
# 		model = Firm 
# 		fields = (
# 			'firm',				
# 			)


class TransactionSerializer(serializers.ModelSerializer):
	#country_from = serializers.Field(source='country_from.countryname')
	quarter = QuarterSerializer()
	# country_from = CountrySerializer()
	# country_to = CountrySerializer()
	corridor = CorridorSerializer()
	# firm = FirmSerializer()
	# rate = RateSerializer()
	class Meta:
		model = Transaction
		fields = (
				'pk',
				'quarter',
				'corridor',
				'rate',
				'firm',
				'fee',
				'ExchangeRateMargin',
				'TotalCostPercent',
				'TotalCostEur',
				'AmountReceived',
				'product_availability',
				'product_availability_icon',
				'transfer_speed_definition',
				'transfer_speed_icon',
				'network_coverage_definition',
				'network_coverage_icon',
			)



    

   
