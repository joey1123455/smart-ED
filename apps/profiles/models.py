from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _ 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

# Create your models here.
class Gender(models.TextChoices):
    MALE = 'Male', _('Male')
    FEMALE = 'Female', _('Female')
    OTHER = 'Other', _('Other')

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User, 
        related_name='profile', 
        on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_('Phone Number'), 
        max_length=30, 
        default="+2348128937115")
    about_me = models.TextField(
        verbose_name=_('About Me'), 
        null=True, 
        blank=False)
    profile_photo = models.ImageField(
        verbose_name=_('Profile Photo'),
        default="/profile_default.png")
    gender = models.CharField(
        verbose_name=_('Gender'),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
        )
    country = CountryField(
        verbose_name=_('Country'),
        default='NG',
        blank=False,
        null=False
        )
    city = models.CharField(
        verbose_name=_('City'),
        default='Abuja',
        blank=False,
        null=False,
        max_length=150,
    )
    school = models.CharField(
        blank=True,
        null=True,
        max_length=300,
    )
    course = models.CharField(
        blank=True,
        null=True,
        max_length=300,
        help_text=_('Whats your Course of study ?')
    )

    def __str__(self):
        return f"{self.user.username}'s profile"