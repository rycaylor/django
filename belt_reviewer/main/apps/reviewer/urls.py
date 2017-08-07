from django.conf.urls import url
from . import views
# from django.contrib import admin
app_name = 'books'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^make$', views.make, name='make'),
    url(r'^page/(?P<id>\d+)$', views.book, name = 'page'),
    url(r'^page/$', views.add_review, name = 'add_review'),
    url(r'^thanks/(?P<id>\d+)$', views.thanks, name = 'thanks'),
    url(r'^profile/(?P<id>\d+)$', views.profile, name = 'profile'),

]
