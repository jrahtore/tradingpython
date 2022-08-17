from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
# from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import generics
from django.contrib import auth
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
# from .decorators import *
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view

# from rest_framework.permissions import IsAuthenticated

from .serializers import RegistrationSerializer,subadminSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import Group



class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # IsAdminUser

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in CustomUser.objects.all()]
        return Response(usernames)
        



class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_type': user.user_type,
            'Create_Clients' : user.Create_Clients,
            'View_Client' :  user.View_Client,
            'Client_Fund' : user.Client_Fund,
            'Clients_Brokerage' : user.Clients_Brokerage,
            'dashboard' : user.dashboard,
            'watchlists' : user.watchlists,
            'username' : user.username,
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'watchlists' : user.watchlists,
            'created_by' : request.user.id,
        })
    
    


@api_view(['POST'])
def registration_tradingclient(request): 
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
    
        if(request.POST.get("View_Client",None) is None or request.data["View_Client"]=='' ):
            view_client = 'no'
        else:
            view_client = request.data["View_Client"] 
        
        
        if(request.POST.get("Client_Fund",None) is None or request.data["Client_Fund"]=='' ):
            client_fund = 'no'
        else:
            client_fund = request.data["Client_Fund"]
        
        
        if(request.POST.get("Clients_Brokerage",None) is None or request.data["Clients_Brokerage"]=='' ):
            clients_brokerage = 'no'
        else:
            clients_brokerage = request.data["Clients_Brokerage"]
        
        
        if(request.POST.get("dashboard",None) is None or request.data["dashboard"]=='' ):
            Dashboard = 'no'
        else:
            Dashboard = request.data["dashboard"]
        
        if(request.POST.get("Create_Clients",None) is None or request.data["Create_Clients"]=='' ):
            create_clients = 'no'
        else:
            create_clients = request.data["Create_Clients"]

        
        if(request.POST.get("watchlists",None) is None or request.data["watchlists"]=='' ):
            Watchlists = ' '
        else:
            Watchlists = request.data["watchlists"]
        
        
       
        userObj = CustomUser(username=request.data["username"],city=request.data["city"],user_type=request.data["user_type"],
        View_Client=view_client,Client_Fund = client_fund,Clients_Brokerage = clients_brokerage,dashboard = Dashboard,Create_Clients = create_clients,watchlists = Watchlists,created_by = request.user)

        



        
    
        userObj.set_password(request.data["password"])
        
     
       
        data = {}
        if serializer.is_valid():
            data_saved = userObj.save()
        #     data_saved.groups.add(Group.objects.get(name='TradingClient'))
        #     data['response'] = "Successfully registered"
        #     data['email'] = data_saved.email
        #     data['username'] = data_saved.username
        #     data['city'] = data_saved.city

        #     token = Token.objects.get(user=data_saved).key
        #     data['token'] = token
        # else:
        #     data = serializer.errors
        # return Response(data)
            return Response("Successfully registered")
        else:
            return Response("this user is already Registered")


@api_view(['POST'])
def registration_subadmin(request): 

    if request.method == 'POST':
        serializer = subadminSerializer(data=request.data)


        if(request.POST.get("View_Client",None) is None or request.data["View_Client"]=='' ):
            view_client = 'no'
        else:
            view_client = request.data["View_Client"] 
        
        
        if(request.POST.get("Client_Fund",None) is None or request.data["Client_Fund"]=='' ):
            client_fund = 'no'
        else:
            client_fund = request.data["Client_Fund"]
        
        
        if(request.POST.get("Clients_Brokerage",None) is None or request.data["Clients_Brokerage"]=='' ):
            clients_brokerage = 'no'
        else:
            clients_brokerage = request.data["Clients_Brokerage"]
        
        
        if(request.POST.get("dashboard",None) is None or request.data["dashboard"]=='' ):
            Dashboard = 'no'
        else:
            Dashboard = request.data["dashboard"]
        
        if(request.POST.get("Create_Clients",None) is None or request.data["Create_Clients"]=='' ):
            create_clients = 'no'
        else:
            create_clients = request.data["Create_Clients"]

        
        if(request.POST.get("watchlists",None) is None or request.data["watchlists"]=='' ):
            Watchlists = ''
        else:
            Watchlists = request.data["watchlists"]
        
       
        clientobj = CustomUser(username=request.data["username"],user_type=request.data["user_type"],
        View_Client=view_client,Client_Fund = client_fund,Clients_Brokerage = clients_brokerage,dashboard = Dashboard,Create_Clients = create_clients,watchlists = Watchlists,created_by = request.user)

        clientobj.set_password(request.data["password"])
        data = {}
        if serializer.is_valid():
            data_saved = clientobj.save()
        #     data_saved.groups.add(Group.objects.get(name='SubAdmin'))
        #     data['response'] = "Successfully registered"
        #     data['email'] = data_saved.email
        #     data['username'] = data_saved.username
        #     token = Token.objects.get(user=data_saved).key
        #     data['token'] = token
        # else:
        #     data = serializer.errors
        # return Response(data)
            return Response("Successfully registered")
        else:
            return Response("this user is already Registered")




@api_view(['POST'])
def registration_superadmin(request): 

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            data_saved = serializer.save()
            data_saved.groups.add(Group.objects.get(name='SuperAdmin'))
            data['response'] = "Successfully registered"
            data['email'] = data_saved.email
            data['username'] = data_saved.username
            token = Token.objects.get(user=data_saved).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)

# added by adil

@ api_view(['DELETE'])
def DeleteCategory(request, pk):
    id = pk
    serializer = CustomUser.objects.get(id=pk)
    serializer.delete()

    return Response({'Deleted Successfully'})
    
@ api_view(['GET'])
def detailusercontentwithid(request, pk):
    Detail = CustomUser.objects.get(id=pk)
    serializer = RegistrationSerializer(Detail)

    return Response(serializer.data)

