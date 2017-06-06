from django.conf.urls import url
from dojo import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)$', views.post_detail, name='post_detail'),
    url(r'^new/', views.post_new, name='post_new'),
    url(r'^(?P<id>\d+)/edit/', views.post_edit, name='post_edit'),
    # url(r'^sum/(?P<x>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    # url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    # url(r'^sum/(?P<args>.*)/$', views.mysum),
    # url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    # url(r'^sum/hello/(?P<name>\w+)/(?P<age>\d+)$', views.hello),
    # url(r'^json_response/$', views.json_reponse),
]
