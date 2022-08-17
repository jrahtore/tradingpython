from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id','user_type','email', 'username',
                    'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('created_by','user_type','watchlists',
         'city','Create_Clients','View_Client','Client_Fund','Clients_Brokerage','dashboard')}),
    )
                
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('Address', 'City',
    #                        'Date_Of_Birth', 'Gender', 'Occupation', 'objective', 'Age', 'Country', 'PostalCode', 'AboutMe')}),
    # )


admin.site.register(CustomUser, CustomUserAdmin)