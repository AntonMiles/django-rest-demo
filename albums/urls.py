from django.conf.urls import url, include
from rest_framework import routers
from albums import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'musicians', views.MusicianViewSet)
router.register(r'albums', views.AlbumViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    ]
