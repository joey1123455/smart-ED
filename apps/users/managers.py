from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 

class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Invalid email address'))
        

    def create_user(self,username,full_name,email,password,**extra_fields):
        if not username:
            raise ValueError(_('Provide a username'))
        if not full_name:
            raise ValueError(_('Provide your full name'))
        if not password:
            raise ValueError(_('Provide a password'))
        if not email:
            raise ValueError(_('Provide your email address'))
        elif email:
            email = self.normalize_email(email)
            self.email_validator(email)
        
        user = self.model(
            username=username, full_name=full_name, password=password,
            email=email, **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user
    

    def create_superuser(self,username,full_name,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusers: is_staff option must be set to true'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusers: is_superuser option must be set to true'))        
        if not password:
            raise ValueError(_('Provide a password'))
        if not email:
            raise ValueError(_('Provide your email address'))
        elif email:
            email = self.normalize_email(email)
            self.email_validator(email)

        user = self.create_user(username, password, email, full_name, **extra_fields)
        user.save(using=self._db)
        return user



