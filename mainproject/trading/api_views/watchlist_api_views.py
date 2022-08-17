from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *


from rest_framework import mixins, generics

from trading.serializers.watchlist_serializer import *

from rest_framework.decorators import api_view

import datetime

from datetime import time



class WatchListAPI(APIView):
	def get(self,request):
		get_watch_list = WatchList.objects.all()
		serializer = WatchListSerializer(get_watch_list,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = WatchListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(UserID=self.request.user)
			return Response({"Message": "Watchlist added"}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
