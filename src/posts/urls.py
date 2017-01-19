from django.conf.urls import include, url
from django.contrib import admin

from .views import (
    posts_list,
    posts_detail,
    posts_delete,
    posts_create,
    posts_update)

urlpatterns = [
    url(r'^$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^(?P<id>\d+)/$', posts_detail),  
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete),
]
