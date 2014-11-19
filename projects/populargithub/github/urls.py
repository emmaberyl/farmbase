from django.conf.urls import patterns, url, include

from github import views
from github.api import RateLimitResource

ratelimit_resource = RateLimitResource()

urlpatterns = patterns('',
    url(r'^queuestatus$', views.QueueStatus, name='QueueStatus'),
    url(r'^api/', include(ratelimit_resource.urls)),
)