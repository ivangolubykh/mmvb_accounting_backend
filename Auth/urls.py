from django.conf.urls import url

from . import views


app_name = 'Auth'
urlpatterns = [
    url(r'^login/$', views.MmvbLoginView.as_view(), name='login'),
    url(r'^logout/$', views.MmvbLogoutView.as_view(), name='logout'),
]
