from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *
from django.db.models.query import QuerySet
import pandas as pd
from rest_framework import mixins, generics
from django.db.models import Count
from trading.serializers.transaction_serializer import detailSerializer
from django.db.models import Count
from rest_framework.decorators import api_view
import datetime

from datetime import time

class UserListingAPI(APIView):


    def get(self,request,format=None):
        detail =  Transaction.objects.all()
        serializer = detailSerializer(detail,many=True)

        return Response(serializer.data)

