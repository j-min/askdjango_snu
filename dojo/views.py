from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import DetailView
from django.db.models import F
from dojo.models import Post


import json

#
# def mysum(request, numbers):
#     numbers = numbers.split('/')
#
#     def convert_fn(num):
#         try:
#             return int(num)
#         except:
#             return 0
#
#     sum_numbers = sum(map(convert_fn, numbers))
#
#     return HttpResponse(sum_numbers)
#
# def hello(reuquest, name, age):
#     return HttpResponse(f"안녕하세요, {name}. {age}살이시네요.")
#
# def json_reponse(request):
#     data = {
#         'message': '안녕, 파이썬&장고',
#         'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
#     }
#     # json_string = json.dumps(data, ensure_ascii=False)
#     # return HttpResponse(json_string, content_type='application/json')
#     return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def post_list(request):

    post_list = Post.objects.all()

    q = request.GET.get('q', '')
    if q:

        post_list = post_list.filter(title__icontains=q)
    # Show max 3 posts
    post_list = post_list[:3]

    return render(request, 'dojo/post_list.html', {
        'post_list': post_list,
    })

def post_detail(request, id):
    Post.objects.filter(id=id).update(hits=F('hits')+1)
    post = get_object_or_404(Post, id=id)
    return render(request, 'dojo/post_detail.html', {
        'post': post
    })
