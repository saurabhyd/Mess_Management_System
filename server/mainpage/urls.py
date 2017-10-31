from django.conf.urls import include,url
from . import views

app_name = 'mainpage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/',include('student.urls')),
]
