from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'get_session_data', views.GetSessionData, basename='session')
router.register(r'issuers', views.IssuerView)
router.register(r'region_fias', views.RegionView)

urlpatterns = [
    path('', include(router.urls)),
]
