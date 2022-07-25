from django.shortcuts import render
from requests import post
from main.models import *
from django.contrib.auth.models import User
from django.core.paginator import Paginator 
# Create your views here.

def mypage(request):
    user = request.user
    post_list = Post.objects.filter(writer=user)
    paginator = Paginator(post_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'users/mypage.html',{'posts':posts})

def mypage2(request):
    user = request.user
    posts = Like.objects.filter(user=user)
    paginator = Paginator(posts,8)
    page = request.GET.get('page')
    like_list = paginator.get_page(page)
    return render(request,'users/mypage2.html',{'like_list':like_list})