from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.trading_serializers import *

from trading.models import *

from trading.serializers.seller_serializer import *

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.pagination import PageNumberPagination

class TradingSymbol(APIView):

	def get(self,request):
		getsymbol = Trading.objects.all()
		serializer = TradingSerializer(getsymbol,many=True)
		return Response(serializer.data)



class TradingSymbolSearch(generics.ListAPIView):
    queryset = Trading.objects.all()
    serializer_class = TradingSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['$trading_symbol']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10