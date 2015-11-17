from django.contrib.auth.models import User
from rest_framework import serializers


class AuthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'date_joined', 'is_superuser', 'last_login')