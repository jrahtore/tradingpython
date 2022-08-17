from trading.models import *

from rest_framework import serializers

class SellerSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserSell
		exclude = ['sellerid']