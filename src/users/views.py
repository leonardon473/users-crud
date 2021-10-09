
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UsersListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
