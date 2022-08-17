# from trading.api_views.brokerage_api_views import brokerage_amount
from rest_framework.decorators import api_view

from trading.models import *

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *
import urllib, json
import os

from rest_framework import mixins, generics

from trading.serializers.transaction_serializer import *

from rest_framework.decorators import api_view

import datetime

from datetime import time


class UserTransactionAPI(APIView):

    def post(self, request, format=None):
        print("post UserTransactionAPI") 
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Usertransaction=self.request.user)
            return Response({"Message": "Transaction Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        print("get UserTransactionAPI")
        getuser = Brokerage_amount.objects.filter(UserWalletID=self.request.user.id).first()
        Transaction.objects.update(brokerage=getuser.Brokerage_amount)
        gettransaction = Transaction.objects.filter(Usertransaction=self.request.user.id)
        serializer = TransactionSerializer(gettransaction, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        print("put UserTransactionAPI")
        gettransaction = Transaction.objects.get(id=pk)

        gettransaction.isClosed = 'yes'
        print(gettransaction.isClosed, "??????????????????????????????")
        if request.data['closeAmount'] is not None:
            print("if")
            print(request.data['closeAmount'])
            if gettransaction.action == "BUY":
                print("iff")
                gettransaction.Brokerage_amount = request.data['Brokerage_amount']

                gettransaction.Close_amount = request.data['closeAmount']
                diff = float(gettransaction.Close_amount) - gettransaction.amount - gettransaction.Brokerage_amount

                gettransaction.difference = diff * gettransaction.quantity
                gettransaction.save()
                create_transaction = Transaction(Usertransaction_id=self.request.user.id,
                                                 sharename=request.data['sharename'], quantity=request.data['quantity'],
                                                 amount=request.data['closeAmount'], action=request.data['action'],
                                                 isClosed='history')
                create_transaction.save()
            else:
                print("else")

                gettransaction.Brokerage_amount = request.data['Brokerage_amount']
                gettransaction.Close_amount = request.data['closeAmount']
                diff = float(gettransaction.Close_amount) - gettransaction.amount - gettransaction.Brokerage_amount

                gettransaction.difference = diff * gettransaction.quantity
                gettransaction.save()
                create_transaction = Transaction(Usertransaction_id=self.request.user.id,
                                                 sharename=request.data['sharename'], quantity=request.data['quantity'],
                                                 amount=request.data['closeAmount'], action=request.data['action'],
                                                 isClosed='history2')
                create_transaction.save()

            getwallet = UserWallet.objects.get(userid=self.request.user.id)
            setwallet = (getwallet.wallet + gettransaction.difference)
            UserWallet.objects.filter(userid=getwallet.userid.id).update(wallet=setwallet)


        gettransaction.save()
        serializer = TransactionSerializer(gettransaction, data=request.data, partial=True)
        print("TTTTTTTTTTTTTTTTTTTTTTTEEEEEEEEEEEEEEEEEESSSSSSSSSSSSTTTTTTTTTT")
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Transaction Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gettransaction = Transaction.objects.get(id=pk)
        gettransaction.delete()
        return Response({"Message": "Transaction Deleted"})


class UserTransactionBuyAPI(APIView):
    
    def get(self, request, format=None):
        print("get UserTransactionBuyAPI")
        getbuy = Transaction.objects.filter(Usertransaction=self.request.user, action='BUY')
        serializer = TransactionSerializer(getbuy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("post UserTransactionBuyAPI")
        print("testyyyyyyyyyyyyyyyyyyyycccccccccccccccccccccccccccccccccccccccccccccccccccc")
        getwallet = UserWallet.objects.get(userid=self.request.user.id)
        getuserid = getwallet.userid
        serializer = TransactionSerializer(data=request.data)

        get_stop_loss_value = request.data['Stop_Loss_Value']
        get_target = request.data['Target_Value']
        getamount = float(request.data['amount'])
        getquantity = int(request.data['quantity'])
        getexact = getamount * getquantity - 10

        if serializer.is_valid():
            serializer.save(Usertransaction=self.request.user, action="BUY", Stop_Loss_Value=get_stop_loss_value,
                            Target_Value=get_target)
            return Response({"Message": "Transaction Buy Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserStopLossTarget(APIView):

    def get(self, request, format=None):
        print("get UserStopLossTarget")
        getbuy = Transaction.objects.filter(Usertransaction=self.request.user, action='BUY')
        getdata(request)
        serializer = TransactionSerializer(getbuy, many=True)
        return Response(serializer.data)


def getdata(request):
    print("get getdata")
    res = Transaction.objects.values_list('sharename', 'amount', 'Target_Value', 'Stop_Loss_Value', 'action').filter(
        isClosed='no')
    for j in res:
        while (a.sharename == None):
            da = '/'
            a.sharename.append(da)

    url = "https://api.datakick.in/REST/quote?API_Key=2e7a9f5610fd0d&m="
    data = (url + da)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
    url = da.to_dict()


def targetBuy(api_sell_price, target):
    print('targetBuyNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
    if (api_sell_price < target):
        isClosed = "yes"
        isClosed = "yes"
        Close_amount = Target_Value


# mark close
def targetSell(api_buy_price, target):
    print('targetSellZZZZZZZZZZZZZZZZZZZZZZZZZZZ')
    if (api_buy_price > target):
        isClosed = "yes"
        status = "yes"
        Close_amount = Target_Value


# mark close
def stoplossBuy(api_sell_price, stoploss):
    print('stoplossBuyXXXXXXXXXXXXXXXXXXXXXXX')
    if (api_sell_price < stoploss):
        isClosed = "yes"
        status = "yes"
        Close_amount = Stop_Loss_Value


# mark close
def stoplossSell(api_buy_price, stoploss):
    print('stoplossSellCCCCCCCCCCCCCCCCC')
    if (api_buy_price > stoploss):
        isClosed = "yes"
        status = "yes"
        Close_amount = Stop_Loss_Value


# mark close
def getdata(request):
    print("??????????????????????????????????????????")
    res = Transaction.objects.values_list('sharename', 'amount', 'Target_Value', 'Stop_Loss_Value', 'action').filter(
        isClosed='no')
    str = [None] * len(res)
    j = 0
    # Creating share value / separated so out put will be NSE:WELINV/NFO:NIFTY21AUGFUT/MCX:GOLD21OCTFUT
    for i in res:
        if i[2] != "" or i[3] != "":
            str[j] = i[0]
        else:
            break
        j = j + 1
    c = '/'.join(str)
    b = 'MCX:' + '/MCX:'.join(str)

    # Creating share value / separated so out put will be NFO:NIFTY21AUGFUT/MCX:GOLD21OCTFUT
    url1 = "https://api.datakick.in/REST/quote?API_Key=2e7a9f5610fd0d&m="
    url = (url1 + b)
    # url = url.strip()
    # url = url.replace(" ","")
    response = urllib.request.urlopen(url)
    data1 = json.loads(response.read())

    x = c.split('/')
    i = 0
    while i < len(x):
        i = i + 1


####################### Transaction API Jitndra #########################################################################
class UserTransactionSellerAPI(APIView):

    def get(self, request, format=None):
        print("UserTransactionSellerAPI getXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        getsell = Transaction.objects.filter(Usertransaction=self.request.user, action='SELL')
        serializer = TransactionSerializer(getsell, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("UserTransactionSellerAPI post........................mmmmmmmmmmmmmmmmmm")
        getwallet = UserWallet.objects.get(userid=self.request.user.id)
        getuserid = getwallet.userid
        serializer = TransactionSerializer(data=request.data)

        get_stop_loss_value = request.data['Stop_Loss_Value']
        get_target = request.data['Target_Value']
        getamount = float(request.data['amount'])
        getquantity = int(request.data['quantity'])

        if serializer.is_valid():
            serializer.save(Usertransaction=self.request.user, action="SELL", Stop_Loss_Value=get_stop_loss_value,
                            Target_Value=get_target)
            return Response({"Message": "Transaction Sell Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CreateTransactionBUY(request, format=None):
    print("ppppppppppppppppppppppppppppppppppp")
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        x = serializer.save(Userid=request.user.id, action='BUY')
        x.save()
    return Response(serializer.data)


@api_view(['POST'])
def CreateTransactionSELLER(request, format=None):
    print("{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(Userid=request.user.id, action='SELL')
    return Response(serializer.data)


class TransactionListingAPI(APIView):

    def get(self, request):
        print("ooooooooooooooooooooooooooooooooooooo")
        gettransactionlist = Transaction.objects.filter(Usertransaction=self.request.user)
        serializer = TransactionListingSerializer(gettransactionlist, many=True)
        return Response(serializer.data)


class TransactionListSearch(generics.ListAPIView):
    serializer_class = TransactionListingSerializer

    def get_queryset(self):
        print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYy111")
        user = self.request.user
        now = datetime.datetime.now().strftime('%H:%M:%S')
        settime = time(23, 59, 58)
        if now >= str(settime):
            print("ifmmmmmmmmmmmmmmmmmmmmmmmmm")
            gettransaction = Transaction.objects.all()
            gettransaction.delete()
        else:
            print("else")
            queryset = Transaction.objects.filter(
                Usertransaction=self.request.user)
            getaction = self.request.query_params.get('isClosed', None)
            print(getaction,"KKKKKKKKKKKKKKKK")
            if getaction is not None:
                queryset = queryset.filter(
                    isClosed=getaction).order_by('updated_at').reverse()
                return queryset
