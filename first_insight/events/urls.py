from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^events/(?P<page_no>[0-9]+)/', views.events, name='events'),
    url(r'^events/', views.event, name='event'),
    url(r'^testing/', views.testing, name='testing'),
    url(r'^get_page/', views.get_page, name='page_no'),
]