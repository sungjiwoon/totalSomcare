from django.conf.urls import url
from . import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    url(r'^$', views.index),
    url(r'^airconditioner/(?P<temp>.+)/$', views.airconditioner),
    url(r'^aircleaner/(?P<air>.+)/$', views.aircleaner),
    url(r'^gas/(?P<gas>.+)/$', views.gascooker),
    url(r'^window/(?P<rain>.+)/$', views.window),
    url(r'^lamp/(?P<motion>.+)/$', views.lamp)   
]
