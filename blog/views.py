from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html')

def post_detail(request, id):
    return HttpResponse(f'{id}번 글을 보고 계십니다.')

def post_edit(request, id):
    pass

def post_delete(request, id):
    pass

def comment_list(request, id):
    pass

def comment_edit(request, id):
    pass

def comment_delete(request, id):
    pass
