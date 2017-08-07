from django.conf.urls import url
from . import views
# from django.contrib import admin
app_name = 'event'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^make_event$', views.make_event, name = 'make_event'),
    # url(r'^logout$', views.logout, name = 'logout'),

]
