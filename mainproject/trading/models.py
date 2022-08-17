from django.db import models

# Create your models here.

from users.models import *

from bulk_update_or_create import BulkUpdateOrCreateQuerySet

class UserWallet(models.Model):
	userid = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
	Created_By =  models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="call")
	wallet = models.FloatField()
	# def __str__(self):
	# 	return f'Created_By :  {self.Created_By} :  UserWalletID : {self.userid}  :  {self.wallet}'
	def __str__(self):
		return str(self.userid) + " : "  + str(self.wallet)

transactionaction = (
	('BUY','BUY'),
	('SELL','SELL'),
	)

isclosed = (

	('yes','yes'),

	('no','no'),

	('history','history'),

	)

class Transaction(models.Model):
	Usertransaction = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	updated_at = models.DateTimeField(auto_now=True)
	sharename = models.CharField(max_length=100)
	quantity = models.IntegerField()
	amount = models.FloatField()
	Brokerage_amount = models.FloatField(null=True,blank=True)
	isClosed = models.CharField(max_length=100,choices = isclosed,default='no')
	Stop_Loss_Value = models.FloatField(null=True,blank=True)
	Target_Value = models.FloatField(null=True,blank=True)
	Close_amount = models.FloatField(null=True,blank=True)
	action = models.CharField(max_length=100, choices = transactionaction)
	difference = models.DecimalField(null=True, blank=True, max_digits=25, decimal_places=5)
	created_by = models.IntegerField()
	status = models.CharField(max_length=100)





buyaction = (
	("BUY" , "BUY"),
	)

class UserBuy(models.Model):
	buyerid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	sharename = models.CharField(max_length=100)
	amount = models.FloatField()
	action = models.CharField(max_length=100,choices = buyaction)


sellaction = (
	("SELL","SELL"),
)

class UserSell(models.Model):
	sellerid = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	sharename = models.CharField(max_length=100)
	amount = models.FloatField()
	action = models.CharField(max_length=100,choices = sellaction)


class Trading(models.Model):
	objects = BulkUpdateOrCreateQuerySet.as_manager()
	trading_symbol = models.CharField(max_length=200)


value = (
	('yes','yes'),
	('no','no'),
	('history','history'),
	)

class WatchList(models.Model):
	UserID = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	Share_Name =models.CharField(max_length=500)
	isClosed = models.CharField(max_length=200, choices = value)

# added by adil

class Fund(models.Model):
	Created_By_id =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	UserWalletID = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="payment")
	total_amount = models.IntegerField()

	def __str__(self):
		return str(self.Created_By_id) + " : "  + str(self.UserWalletID)

	# def __str__(self):
	# 	return f'Created_By :  {self.Created_By}  : UserWalletID : {self.UserWalletID}'

# added by adil

class Brokerage_amount(models.Model):
	Created_By_id =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	UserWalletID = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="wallet",unique=True)
	Brokerage_amount = models.IntegerField()

	def __str__(self):
		return str(self.Created_By_id) + " : "  + str(self.UserWalletID)
	# def __str__(self):
	# 	return f'Created_By :  {self.Created_By} :  UserWalletID : {self.UserWalletID}'
