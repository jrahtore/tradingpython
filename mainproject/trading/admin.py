from django.contrib import admin

# Register your models here.
from .models import *

# added by adil 
admin.site.register(Fund)

# added by adil 
@admin.register(Brokerage_amount)
class Brokerage_amountAdmin(admin.ModelAdmin):
	list_display = ['id','Created_By_id','UserWalletID','Brokerage_amount']


@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
	list_display = ['userid','wallet']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = ['id','Usertransaction','sharename','amount','quantity','action','isClosed','Close_amount','difference']
	

@admin.register(UserBuy)
class BuyerAdmin(admin.ModelAdmin):
	list_display = ['buyerid','sharename','amount','action']

Trading

@admin.register(UserSell)
class SellerAdmin(admin.ModelAdmin):
	list_display = ['sellerid','sharename','amount','action']


@admin.register(Trading)
class TradingAdmin(admin.ModelAdmin):
	list_display = ['id','trading_symbol']


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
	list_display = ['id','UserID','Share_Name','isClosed']