from django.conf.urls import patterns, url, include
from github import views

urlpatterns = patterns('',
    url(r'^queuestatus$', views.QueueStatus, name='QueueStatus'),
    url(r'^populate$', views.populate, name='populate'),
)