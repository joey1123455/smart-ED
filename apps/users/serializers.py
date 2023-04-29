from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from .models import User

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(source='get_full_name')
    gender = serializers.CharField(source='profile.gender')
    phone_number = PhoneNumberField(source='profile.phone_number')
    profile_photo = serializers.ImageField(source='profile.profile_photo')
    country = CountryField(source='profile.country')
    city = serializers.CharField(source='profile.city')
    course = serializers.CharField(source='profile.course')
    school = serializers.CharField(source='profile.school')

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 
                  'gender', 'country', 'city',
                  'course', 'school', 'phone_number', 
                  'profile_photo', 'email'
                  ]
    def to_representation(self, instance):
        representation = super(UserSerializer).to_representation(instance)
        if instance.is_superuser:
            representation['admin'] = True
        return representation
    

class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'password']
