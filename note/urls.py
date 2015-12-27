from django.conf.urls import include, url
from . import views
from . import views_new

urlpatterns = [

	url(r'^$', views.post_list),
	url(r'^wypelnienie.html$', views_new.post_list_new),

]