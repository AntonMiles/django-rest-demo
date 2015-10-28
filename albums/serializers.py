__author__ = 'anton'
from django.contrib.auth.models import User, Group
from albums.models import Musician, Album
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'first_name', 'last_name', 'is_staff', 'is_active',
                  'date_joined', 'is_superuser', 'last_login')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MusicianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Musician
        fields = ('first_name', 'last_name', 'instrument')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('artist', 'name', 'release_year', 'num_stars')
