from django.shortcuts import render
import os
from django.conf import settings

from django.views.generic import View

# from django.https import HttpResponse

# Create your views here.

def post_list1(request):
    name='공유'
    response = render(request, 'myapp/post_list.html',
        {'name':name})
    return response

def image_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'geunhye.jpg')


class SampleTemplateView(object):
    @classmethod
    def as_view(cls, template_name):
        def view_fn(request):
            return render(request, template_name)
        return view_fn

fbv_view = SampleTemplateView.as_view('myapp/sample_template.html')

# url로 이름을 받아서
# 흰색 배경 까만 글씨 이미지를 만들어서
# 이미지를 다운로드받기
# PIL / pillow / wand 사용해보기
# views.py urls.py 제출





def excel_download(request):
    filepath = '/'
    pass
