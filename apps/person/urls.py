from django.conf.urls import patterns, url
from apps.person import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'create$', views.create, name='create'),
	url(r'new$', views.new, name='new'),
	url(r'^person/(?P<person_id>\d+)/delete$', views.delete, name='delete'),
	url(r'^person/(?P<person_id>\d+)/edit$', views.edit, name='edit'),
	url(r'update$', views.update, name='update'),
	url(r'^person/(?P<person_id>\d+)/profile$', views.profile, name='profile'),
)