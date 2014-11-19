from django.conf.urls import patterns, url, include

from github import views
from github.api import RateLimitResource

ratelimit_resource = RateLimitResource()

urlpatterns = patterns('',
    #url(r'^$', views.populate, name='QueueStatus'),
    url(r'^api/', include(ratelimit_resource.urls)),
)