from rest_framework.views import APIView



from rest_framework.response import Response



from rest_framework import status



from users.models import CustomUser

from trading.models import UserWallet

from trading.models import UserBuy
from trading.models import UserSell

from trading.serializers.custom_api import *

from trading.models import Transaction

from rest_framework.decorators import api_view



from rest_framework.response import Response



from rest_framework import status



from rest_framework.views import APIView



from rest_framework import mixins, generics



from rest_framework.decorators import api_view

import json

from django.http import HttpResponse, JsonResponse



from django.core import serializers

class GetUserAPI(APIView):



    def get(self,request,format=None):



        user = CustomUser.objects.filter(username= request.user).values_list('user_type' , flat=True).first()
        user_type = self.request.query_params.get('user_type')

        if user_type == "super_admin" or user == "super_admin":


            getuser = CustomUser.objects.filter(user_type='trading_client')

        else:

            getuser = CustomUser.objects.filter(user_type='trading_client',created_by = self.request.user)


        ret = []

        count = 0

        for i in getuser:


            w = 0

            wallet = UserWallet.objects.filter(userid=i.id).first()

            if wallet is not None:

                w = wallet.wallet

            tranaction = Transaction.objects.filter(Usertransaction=i.id)
        
            tranaction = serializers.serialize("json", tranaction)
            
            check = json.dumps(tranaction)
            
            check2 = json.loads(check.replace("\'", '"'))
            
            check3 = json.loads(check2.replace("\'", '"'))


            temp = {"id" : i.id,"username":i.username,"first_name":i.first_name,"last_name":i.last_name,"email":i.email,"wallet":w,"city":i.city,"transaction": check3}


            ret.append(temp)

            count += 1




        return JsonResponse(ret, safe=False)

