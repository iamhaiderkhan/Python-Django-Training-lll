from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, UserEducationInfoViewSet, DegreeVerifyViewSet

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'education', UserEducationInfoViewSet)
router.register(r'verify-degree', DegreeVerifyViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]