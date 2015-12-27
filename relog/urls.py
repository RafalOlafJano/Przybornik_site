from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^login/$', views.post_login, name = 'post_login'),

#	url(r'^logged_out/', views.post_loggedout, name = 'post_loggedout'),

]


#from django.conf.urls import patterns, include, url
