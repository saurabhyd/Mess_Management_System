from django.conf.urls import url
from . import views

app_name= 'student'

urlpatterns = [
    #url(r'^/(?P<details>[^\/]*)/$', views.details, name='details'),
    url(r'^(?P<usid>[0-9][0-9][A-Z][A-Z][0-9][0-9]+)/$', views.details, name='details'),
    #url(r'^$',views.details,name='details')

    url(r'^(?P<usid>[0-9][0-9][A-Z][A-Z][0-9][0-9]+)/studentfeedback/$', views.feedback, name='feedback'),

]
