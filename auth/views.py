from django.contrib.auth.models import User
from rest_framework import viewsets
from auth.serializers import AuthSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = AuthSerializer


class ConfirmViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
