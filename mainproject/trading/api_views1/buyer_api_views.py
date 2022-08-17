from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *

from trading.serializers.buyer_serializers import *


class UserBuyAPI(APIView):

	def post(self,request,format=None):
		serializer = BuyerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(buyerid = self.request.user)
			return Response({"Message": "Buy Created"}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self,request,format=None):
		getbuyer = UserBuy.objects.filter(buyerid=self.request.user.id)
		serializer = BuyerSerializer(getbuyer,many=True)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		getbuyer = UserBuy.objects.get(id=pk)
		serializer  = BuyerSerializer(getbuyer, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"Message": "Buy Updated"})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		getbuyer = UserBuy.objects.get(id=pk)
		getbuyer.delete()
		return Response({"Message": "Buy Deleted"})