from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<text>[ㄱ-힣]+)/$', views.download_image)
]
