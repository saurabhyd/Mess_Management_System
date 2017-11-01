from django.conf.urls import url
from . import views

app_name = 'adminpage'

urlpatterns = [
    url(r'^$', views.admin, name='admin'),
    url(r'^adminlogin/(?P<aid>[0-9]+)$', views.manageadmin, name='adminlogin'),
]
