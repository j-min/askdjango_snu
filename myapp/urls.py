from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list1),
    url(r'^sample/$', views.fbv_view)
]
