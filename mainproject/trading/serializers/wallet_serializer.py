from trading.models import *

from rest_framework import serializers


class UserWalletSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserWallet
		# exclude = ['userid']
		exclude = ['Created_By']
		depth = 1

class detailWalletSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserWallet
		fields = '__all__'
		depth = 1
		# fields = '__all__'