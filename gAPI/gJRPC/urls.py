from django.conf.urls import patterns, include, url
from . import views
from jsonrpc import jsonrpc_site

name='gJRPC'
urlpatterns =  [
	url(r'^$', views.home),
	url(r'^jrpc_test/$', jsonrpc_site.dispatch, name="jrpc_test"),
]
