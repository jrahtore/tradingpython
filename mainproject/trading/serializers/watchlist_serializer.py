from trading.models import *

from rest_framework import serializers



class WatchListSerializer(serializers.ModelSerializer):
	class Meta:
		model = WatchList
		fields = "__all__"