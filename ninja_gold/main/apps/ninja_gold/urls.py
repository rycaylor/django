from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process),
    url(r'^reset$', views.reset),
]
