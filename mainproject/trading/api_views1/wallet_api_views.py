from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *


class UserWalletAPI(APIView):
	# Added by adil

	def post(self,request):
		serializer = UserWalletSerializer(data=request.data)
		if serializer.is_valid():
			getfund = UserWallet.objects.filter(userid = request.POST["userid"]).first()
				
			if getfund is not None:
				getdata = getfund.wallet +int(request.data['wallet']) 
				saveData = UserWallet.objects.filter(id = getfund.id).update(wallet=getdata)
			else:
				saveData = UserWallet.objects.create(wallet=request.POST['wallet'],
				userid=CustomUser(id=request.POST["userid"]),Created_By_id=request.user.id)
			return Response({"Message": "Wallet Updated"}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



	def get(self,request,format=None):
		getuser = UserWallet.objects.get(userid=self.request.user.id)
		serializer = UserWalletSerializer(getuser)
		return Response(serializer.data)

	def put(self,request,pk,format=None):
		getuser = UserWallet.objects.get(id=pk)
		serializer  = UserWalletSerializer(getuser, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"Message": "Wallet Updated"})
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		getuser = UserWallet.objects.get(id=pk)
		getuser.delete()
		return Response({"Message": "UserWallet Deleted"})