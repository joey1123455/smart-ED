from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'pkid', 'user', 'gender', 'phone_number', 'course', 'school', 'city', 'country']
    list_filter = ['gender', 'country', 'school', 'course']
    list_display_links = ['id', 'pkid', 'user']


admin.site.register(Profile, ProfileAdmin) 