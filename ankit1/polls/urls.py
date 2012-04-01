from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('polls.views',
    #url(r'^$', 'index'),
	
	url(r'^login', 'login_view'),
	#url(r'^login', 'login_view'),
	url(r'^welcome', 'index'),
	#url('abc/login_view', 'login_view'),
	#url('abc/loginSuccessful', 'index'),
	url(r'^logout','logout_view'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)