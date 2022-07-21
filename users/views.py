from django.shortcuts import render
from requests import post
from main.models import *
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    user = request.user
    posts = Post.objects.filter(writer=user)
    return render(request,'users/mypage.html',{'posts':posts})

def mypage2(request):
    user = request.user
    like_list = Like.objects.filter(user=user)
    posts = Post.objects.filter(writer=user)
    return render(request,'users/mypage2.html',{'posts':posts, 'like_list':like_list})