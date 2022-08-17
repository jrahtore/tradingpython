from users.models import CustomUser

from django.contrib.auth.hashers import make_password

from rest_framework.serializers import *


class CustomUserSerializer(ModelSerializer):
	class Meta:
		model = CustomUser
		fields = "__all__"
		# depth = 1

	def __init__(self, *args, **kwargs):
		kwargs['partial'] = True
		super(CustomUserSerializer, self).__init__(*args, **kwargs)

class CustomUserSerializer2(ModelSerializer):
	class Meta:
		model = CustomUser
		fields = "__all__"
		
