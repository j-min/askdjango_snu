from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import DetailView
from dojo.models import Post
import json

# Create your views here.

# def mysum(request, numbers):
#     numbers = map(int, numbers.split('/'))
#     sum_numbers = sum(numbers)
#     return HttpResponse(sum_numbers)

def mysum(request, numbers):
    numbers = numbers.split('/')

    def convert_fn(num):
        try:
            return int(num)
        except:
            return 0

    sum_numbers = sum(map(convert_fn, numbers))

    return HttpResponse(sum_numbers)

def hello(reuquest, name, age):
    return HttpResponse(f"안녕하세요, {name}. {age}살이시네요.")

def json_reponse(request):
    data = {
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }
    # json_string = json.dumps(data, ensure_ascii=False)
    # return HttpResponse(json_string, content_type='application/json')
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


class post_detail(DetailView):
    model = Post
    template_name = 'dojo/post_detail.html'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        self.object.hits+=1
        self.object.save()
