"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from login.views import ListUsers, CustomAuthToken

from login.views import registration_tradingclient , registration_subadmin , registration_superadmin ,DeleteCategory,detailusercontentwithid

admin.site.site_header = "Trading ADMIN PANEL"
admin.site.site_title = "Trading ADMIN PORTAL"
admin.site.index_title = "Welcome to Mhd Adil Khan"



urlpatterns = [

    path('admin/', admin.site.urls),
    path('trading/', include('trading.urls')),
    # path('recordandcoin/', include('mainproject.urls')),
    # path('', include('login.urls')),
    path('api/users/', ListUsers.as_view()),
    path('api/token/', CustomAuthToken.as_view()),
    path('api/register_tradingclient/', registration_tradingclient, name='registertradingclient'),
    path('api/register_subadmin/', registration_subadmin, name='registersubadmin'),
    path('api/register_superadmin/', registration_superadmin, name='registersuperadmin'),
    
    path('api/delete_users/<int:pk>/', DeleteCategory, name='delete_superadmin'),
    
    path('api/detail_users_id/<int:pk>/', detailusercontentwithid, name='detailusercontentwithid_superadmin'),
]
