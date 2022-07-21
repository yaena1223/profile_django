from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/',mypage,name="mypage"),
    path('mypage2/',mypage2,name="mypage2"),
    
]