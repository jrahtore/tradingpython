from trading.models import *

from rest_framework.serializers import *

class FundSerializer(ModelSerializer):
	class Meta:
		model = Fund
		# fields = "__all__"
		exclude = ['Created_By_id']
		