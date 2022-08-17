from trading.models import *

from rest_framework import serializers

class BuyerSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserBuy
		exclude = ['buyerid']