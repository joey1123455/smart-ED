from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    fullname = serializers.CharField(source='user.full_name')
    email = serializers.EmailField(source='user.email')
    country = CountryField(name_only=True)
    
    class Meta:
        model = Profile
        fields = ['username', 'fullname', 'email', 'phone_number',
                  'about_me', 'profile_photo', 'gender', 'school',
                  'course', 'country', 'city', ]
        

class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ['phone_number','about_me', 
                  'profile_photo', 'gender',
                  'school', 'course', 
                  'country', 'city',]
        

