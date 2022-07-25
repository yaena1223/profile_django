from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 

import json
# Create your views here.
def showmain(request):
    post = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'main/mainpage.html',{'post':post,'posts':posts})

def post(request):
    post = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'main/post.html',{'post':post,'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    paginator = Paginator(all_comments,5)
    page = request.GET.get('page')
    comments = paginator.get_page(page)
    return render(request, 'main/detail.html', {'post':post, 'comments':comments})


def new(request):
    return render(request, 'main/new.html')



def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def edit(request,id):
    edit_post = Post.objects.get(id=id)
    return render(request,'main/edit.html', {'post':edit_post})

def update(request,id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer= request.user
    update_post.pub_date = timezone.now()
    update_post.body = request.POST['body']
    if request.FILES.get("image"):
        update_post.image = request.FILES.get('image')
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:showmain')

def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk = post_id)
    new_comment.save() 
    return redirect('main:detail', post_id)


def edit_comment(request,comment_id):
    edit_comment = Comment.objects.get(id = comment_id)
    return render(request,'main/edit_comment.html',{'comment':edit_comment})

def update_comment(request,comment_id):
    update_comment = Comment.objects.get(id = comment_id)
    update_comment.writer = request.user
    update_comment.content = request.POST['content']
    update_comment.save()
    return redirect('main:detail',update_comment.post.id)



def delete_comment(request,comment_id):
    delete_comment = Comment.objects.get(id=comment_id)
    delete_comment.delete()
    return redirect('main:detail',delete_comment.post.id)


# 3. like_toggle 함수 작성하기
@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user=request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "like_cancel"
    else:
        result = "like"
    context = {
        "like_count" : post.like_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")



@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user=request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "dislike_cancel"
    else:
        result = "dislike"
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }
    return HttpResponse(json.dumps(context), content_type = "application/json")

