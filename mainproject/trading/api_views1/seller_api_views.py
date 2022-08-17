from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *

from trading.serializers.seller_serializer import *


class UserSellerAPI(APIView):

	def post(self,request,format=None):
		serializer = SellerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(sellerid = self.request.user)
			return Response({"Message": "Sell Created"}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self,request,format=None):
		getseller = UserSell.objects.filter(sellerid = self.request.user.id)
		serializer = SellerSerializer(getseller,many=True)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		getseller = UserSell.objects.get(id=pk)
		serializer  = SellerSerializer(getseller, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"Message": "Sell Updated"})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		getseller = UserSell.objects.get(id=pk)
		getseller.delete()
		return Response({"Message": "Sell Deleted"})