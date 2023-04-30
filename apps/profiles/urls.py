from django.urls import path
from .views import (
    GetProfileAPIView, UpdateProfileApiView
)

urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name='get-profile'),
    path('update/<str:username>/', UpdateProfileApiView.as_view(), name='update_profile'),
]
