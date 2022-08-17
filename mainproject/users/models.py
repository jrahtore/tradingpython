from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('super_admin', 'super_admin'),
        ('sub_admin', 'sub_admin'),
        ('trading_client', 'trading_client'),
    )
    Create_value = (
	('yes','yes'),
	('no','no'),
    )

    user_type = models.CharField(max_length=150 ,choices=STATUS_CHOICES,null=False,blank=False)
    city = models.CharField(max_length=100)
    watchlists = models.TextField(max_length=150 ,default='',blank=True)
    Create_Clients = models.CharField(max_length=150 ,choices= Create_value,default='no')
    View_Client = models.CharField(max_length=150 ,choices= Create_value,default='no')
    Client_Fund = models.CharField(max_length=150 ,choices= Create_value,default='no')
    Clients_Brokerage = models.CharField(max_length=150 ,choices= Create_value,default='no')
    dashboard = models.CharField(max_length=150 ,choices= Create_value,default='no')
    created_by = models.ForeignKey('self',on_delete=models.CASCADE,null = True,blank=True)

    class Meta:
        db_table = 'auth_user'


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
