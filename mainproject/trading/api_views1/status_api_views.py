from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *


from rest_framework import mixins, generics

from trading.serializers.transaction_serializer import *

from rest_framework.decorators import api_view

import datetime

from datetime import time


class StatusAPI(APIView):

	def get(self,request,format=None):
	    
	    id = self.request.query_params.get('id')
	    
	    user_type = self.request.query_params.get('user_type')
	    
	    if user_type == "super_admin":
	        getbuy = Transaction.objects.filter(isClosed = 'no')
	    else:
	        getbuy = Transaction.objects.filter(status = 'no', created_by = id )
	    serializer = StatusSerializer(getbuy,many=True)
	    return Response(serializer.data)
	        
		
		
