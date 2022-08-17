from django.shortcuts import render

# Create your views here.
from django_pandas.io import read_frame

from bulk_update_or_create import BulkUpdateOrCreateQuerySet

import bulk_update_or_create

import pandas as pd

from .models import Transaction

#added by adil

import urllib, json
import requests

from .models import Trading, Transaction

from django.http import HttpResponse

from rest_framework.response import Response

def savedata(request):
	getfile = pd.read_csv('https://api.datakick.in/NFO/list/NFO.csv')
	df = getfile['tradingsymbol']
	df = df.to_dict()
	trade = Trading.objects.all()
	trade.delete()
	trading_symbol_instances = [Trading(
            trading_symbol=record,

        ) for x, record in df.items()]
	Trading.objects.bulk_update_or_create(trading_symbol_instances,['trading_symbol'],match_field=['trading_symbol'])
	return HttpResponse("Data is Saved")


# new function added


####################### Transaction API Jitndra ############################################################
def targetBuy(api_sell_price,target,id):
	print("api_sell_price")
	print(api_sell_price)
	if(api_sell_price<target):
		isClosed = "yes"
		isClosed = "yes"
		Close_amount = target
		saveAmt(id,Close_amount)
		#mark close
def targetSell(api_buy_price,target,id):
    print("api_sell_price1")
    if(api_buy_price>target):
	    isClosed = "yes"
	    Close_amount = target
	    saveAmt(id,Close_amount)
		#mark close
def stoplossBuy(api_sell_price,stoploss,id):
    print("api_sell_price2")
    if(api_sell_price<stoploss):
        isClosed = "yes"
        Close_amount = stoploss
        saveAmt(id,Close_amount)
		#mark close
def stoplossSell(api_buy_price,stoploss,id):
    print("api_sell_price3")
    if(api_buy_price>stoploss):
        isClosed = "yes"
        Close_amount = stoploss
        saveAmt(id,Close_amount)

		#mark close
def saveAmt(id,amt):
	Transaction.objects.filter(id=id).update(amount=amt,isClosed="yes")
def getdata(request):

	res = Transaction.objects.values_list('sharename','amount','Target_Value','Stop_Loss_Value','action','id').filter(isClosed='no')
	print("#################")
	print(res)
	import re

	slash = "/"
	da = ""
	mcxArr = ["GOLD","SILVER","CRUDEOIL","COPPER","ZINC","NICKEL"]
	for a in res:
		r = re.compile("([a-zA-Z]+)([0-9]+)")
		m = r.match(a[0])
		if(m.group(1) in mcxArr):
			da = da+"MCX:"+ a[0]+slash
		else:
			da = da+"NFO:"+ a[0]+slash


	url = "https://api.datakick.in/REST/quote?API_Key=2e7a9f5610fd0d&m="
	url = (url + da)
	response = urllib.request.urlopen(url)
	data = json.loads(response.read())
	data = data["data"]
	print(url)
	print("url")
	for a in res:
		print("hello")

		if(a[0] in data):
			share_api = data[a[0]]
			action = a[4]

			if(action == "BUY"):

				if a[2]:


					targetBuy(share_api["buy"],a[2],a[5])
					#targetBuy(45864,a[2],[5])
				if a[3]:

					stoplossBuy(share_api["buy"],a[3],a[5])

			if(action == "SELL"):
				if a[2]:
					targetSell(share_api["sell"],a[2],a[5])
				if a[3]:
					stoplossBuy(share_api["sell"],a[3],a[5])

	return HttpResponse("Data is Saved")


####################### Transaction API Jitndra ############################################################
