from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJsonRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer

# Create your views here.

class GetProfileAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJsonRenderer]

    def get(self,request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(
            user_profile, context={'request':request}
            )
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UpdateProfileApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJsonRenderer]
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile
        
        data = request.data 
        serializer = UpdateProfileSerializer(
            instance=request.user.profile,
            data=data, partial=True 
            )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)