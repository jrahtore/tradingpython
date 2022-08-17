from trading.models import *

from rest_framework import serializers

from trading.models import Transaction




class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		exclude = ['Usertransaction','action']





class TransactionListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		kwargs['partial'] = True
		super(TransactionListingSerializer, self).__init__(*args, **kwargs)

class detailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		# fields = '__all__'
		fields = ['Usertransaction','sharename','amount','difference','action','quantity','Close_amount','Brokerage_amount']
		depth = 1
		

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'
		depth = 1
	