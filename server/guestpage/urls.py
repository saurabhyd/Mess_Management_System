from django.conf.urls import url
from . import views

app_name = 'guestpage'

urlpatterns = [
    url(r'^$', views.guest, name='guest'),
]
