from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.show_check, name='show_check'),
	]