from django.conf.urls import url
from . import views
# from django.contrib import admin
app_name = 'ds'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^post$', views.post, name = 'post'),
    url(r'^like/(?P<id>\d+)$', views.like, name = 'like'),
    url(r'^unlike/(?P<id>\d+)$', views.unlike, name = 'unlike'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete'),
    url(r'^mostpopular$', views.mostpopular, name = 'mostpop'),

]
