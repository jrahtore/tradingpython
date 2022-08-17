from rest_framework import serializers

from trading.models import *

class TradingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trading
		fields = "__all__"