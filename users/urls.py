from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage/<int:id>/',mypage,name="mypage"),
    path('mypage2/<int:id>/',mypage2,name="mypage2"),
    path('follow/<int:id>', follow, name = "follow"),
    
]