from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import DetailView
from django.db.models import F
from dojo.models import Post
from django.utils import timezone
from .forms import PostForm
import datetime

# dojoviews.py
def post_list(request):
    post_list = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        post_list = post_list.filter(title__icontains=q)
    # Show max 3 posts
    post_list = post_list[:3]

    return render(request, 'dojo/post_list.html', {
        'q': q,
        'post_list': post_list,
    })

def post_detail(request, id):
    Post.objects.filter(id=id).update(hits=F('hits')+1)
    post = get_object_or_404(Post, id=id)
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()
    prev_post = Post.objects.filter(id__gt=post.id).order_by('-id').first()
    return render(request, 'dojo/post_detail.html', {
        'post': post,
        'next_post': next_post,
        'prev_post': prev_post,
    })

def archives(request):
    day_list = []
    start = datetime.datetime(2017, 1, 1)
    for i in range(365):
        delta = datetime.timedelta(days=i)
        days_list.append(start+delta)

    return render(request, 'dojo/archives.html', {
        'day_list': day_list,})

def post_new(request):
    if request.method == 'GET':
        form = PostForm()
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('VALID !!!')
            print(form.cleaned_data)  # dict
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save() # ModelForm에서만 지원하는 함수
            return redirect('dojo:post_detail', id=post.id)

    return render(request, 'dojo/post_form.html', {'form': form})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        form = PostForm(instance=post)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('dojo:post_detail', id=post.id)

    return render(request, 'dojo/post_form.html', {'form': form})
