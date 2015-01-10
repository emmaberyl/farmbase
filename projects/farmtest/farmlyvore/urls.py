from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from farmlyvore import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^farmlyvore/search', views.search, name='search'),
    

)
urlpatterns += staticfiles_urlpatterns()
