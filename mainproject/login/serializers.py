from users.models import CustomUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class subadminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password','user_type','dashboard','Create_Clients','View_Client','Client_Fund','Clients_Brokerage','created_by']



class RegistrationSerializer(serializers.ModelSerializer):

    # password2 = serializers.CharField(
    #     style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name','city' , 'user_type','created_by']
        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }

    # def save(self):
    #     account = CustomUser(
    #         email=self.validated_data['email'],
    #         username=self.validated_data['username'],
    #         first_name=self.validated_data['first_name'],
    #         last_name=self.validated_data['last_name'],
    #         Address=self.validated_data['Address'],
    #         City=self.validated_data['City'],
    #         Date_Of_Birth=self.validated_data['Date_Of_Birth'],
    #         Gender=self.validated_data['Gender'],
    #         Occupation=self.validated_data['Occupation'],
    #         objective=self.validated_data['objective'],
    #         Age=self.validated_data['Age'],
    #         Country=self.validated_data['Country'],
    #         PostalCode=self.validated_data['PostalCode'],
    #         AboutMe=self.validated_data['AboutMe'],
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']

    #     if password != password2:
    #         raise serializers.ValidationError(
    #             {'password': 'Passwords must match.'})
    #     account.set_password(password)
    #     account.save()
    #     return account
