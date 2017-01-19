from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.posts_list),
    url(r'^create/$', views.posts_create),
    url(r'^detail/$', views.posts_detail),
    
    url(r'^update/$', views.posts_update),
    url(r'^delete/$', views.posts_delete),
]
