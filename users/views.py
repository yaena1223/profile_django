from django.shortcuts import get_object_or_404, render, redirect
from requests import post
from main.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator 
# Create your views here.

def mypage(request, id):
    user = get_object_or_404(User,pk = id)
    post_list = Post.objects.filter(writer=user)
    paginator = Paginator(post_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'users/mypage.html',{'posts':posts, 'user':user})

def mypage2(request, id):
    user = get_object_or_404(User,pk = id)
    posts = Like.objects.filter(user=user)
    paginator = Paginator(posts,8)
    page = request.GET.get('page')
    like_list = paginator.get_page(page)
    return render(request,'users/mypage2.html',{'like_list':like_list, 'user':user})

def follow(request, id):
    user=request.user
    followed_user=get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)
