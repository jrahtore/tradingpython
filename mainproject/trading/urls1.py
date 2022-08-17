from django.urls import path

from . import views

from trading.api_views import wallet_api_views , transaction_api_views , buyer_api_views , seller_api_views , trading_api_views , watchlist_api_views,custom_api_views,fund_api_views,brokerage_api_views,getuser_api_views,listing_api_views,subadmin_api_views,target_api_views,status_api_views,detail_api_views


urlpatterns = [

	path('wallet/',wallet_api_views.UserWalletAPI.as_view()),
	path('wallet/<int:pk>/',wallet_api_views.UserWalletAPI.as_view()),

    path('target/<int:pk>/',target_api_views.TargetAPI.as_view()),
    path('delete/',target_api_views.DeleteAPI.as_view()),
	path('detail_balance/',detail_api_views.detailAPI.as_view()),

	path('transaction_status/',status_api_views.StatusAPI.as_view()),
	path('transaction_status/<int:pk>/',status_api_views.StatusAPI.as_view()),

	path('transaction/',transaction_api_views.UserTransactionAPI.as_view()),
	path('transaction/<int:pk>/',transaction_api_views.UserTransactionAPI.as_view()),
	path('buyer/',buyer_api_views.UserBuyAPI.as_view()),
	path('buyer/<int:pk>/',buyer_api_views.UserBuyAPI.as_view()),
	path('seller/',seller_api_views.UserSellerAPI.as_view()),
	path('seller/<int:pk>/',seller_api_views.UserSellerAPI.as_view()),
	path('transactionbuy/',transaction_api_views.UserTransactionBuyAPI.as_view()),
	path('stopLossTarget/',transaction_api_views.UserStopLossTarget.as_view()),
	path('transactionsell/',transaction_api_views.UserTransactionSellerAPI.as_view()),
	path('transactionlist/',transaction_api_views.TransactionListingAPI.as_view()),
	path('watchlist/',watchlist_api_views.WatchListAPI.as_view()),
	path('data/',custom_api_views.CustomUserAPI.as_view()),
	#search_api
	path('transactionsearch/',transaction_api_views.TransactionListSearch.as_view()),
	path('trading_symbol/',trading_api_views.TradingSymbol.as_view()),
	path('symbol_search/',trading_api_views.TradingSymbolSearch.as_view()),
	path('save_data/',views.savedata,name='save_data'),


	# added by adil
	path('filter/',views.getdata,name='filter_data'),

	path('Brokerage_detail/' ,brokerage_api_views.brokerage_amount, name='brokerage_detail'),

	path('data/<str:pk>/', custom_api_views.CustomUserAPI.as_view()),

	path('trading_client', getuser_api_views.GetUserAPI.as_view()),

	path('getusers', subadmin_api_views.GetsubadminAPI.as_view()),

	#added by adil

	path('fund/',fund_api_views.FundAPI.as_view()),

	path('fund/<str:pk>/', fund_api_views.FundAPI.as_view()),


	path('brokerage/',brokerage_api_views.Brokerage_amountAPI.as_view()),

	path('brokerage/<str:pk>/', brokerage_api_views.Brokerage_amountAPI.as_view()),
    
	path('list_users/',listing_api_views.UserListingAPI.as_view()),
]
