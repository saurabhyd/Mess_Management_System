from django.conf.urls import url
from . import views

app_name= 'messmenu'

urlpatterns = [
    url(r'^$', views.messmenu, name='messmenu'),
]
