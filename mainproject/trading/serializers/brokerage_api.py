from trading.models import *


from rest_framework.serializers import *


class Brokerage_amountSerializer(ModelSerializer):
	class Meta:
		model = Brokerage_amount
		# fields = "__all__"

		exclude = ['Created_By_id']
		