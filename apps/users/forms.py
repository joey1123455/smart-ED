from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meat(UserCreationForm):
        model = User
        fields = ['email', 'username', 'full_name']
        error_class = 'error'


class CustomUserChangeForm(UserChangeForm):
    class Meat(UserCreationForm):
        model = User
        fields = ['email', 'username', 'full_name']
        error_class = 'error'

        