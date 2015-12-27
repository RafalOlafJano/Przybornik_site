from django.conf.urls import include, url
from django.contrib import admin
from contact import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('menu.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^relog/', include('relog.urls')),
    url(r'^find/', include('find.urls')),



    url(r'^pollster/', include('pollster.urls')),
    url(r'^note/', include('note.urls')),

    url(r'^timetable/', include('timetable.urls')),
    url(r'^guestbook/', include('guestbook.urls')),


    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': 'http://127.0.0.1:8000/'}),

]