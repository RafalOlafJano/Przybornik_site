from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^$', views.post_list, name = 'post_list'),

	url(r'^find_note/', views.post_note, name = 'post_note'),

	url(r'^find_guestbook/', views.post_guestbook, name = 'post_guestbook'),
	
	url(r'^find_pollster/', views.post_pollster, name = 'post_pollster'),

	url(r'^find_timetable/', views.post_timetable, name = 'post_timetable'),

]