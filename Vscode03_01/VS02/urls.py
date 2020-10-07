from django.urls import path
from . import views

urlpatterns=[
    # 이 urls.py로 들어왔을 때 가장 먼저 보여져야할 페이지는 views에 있는 index함수의 return 값이다.
    path('', views.index),
    # 마지막 요청값이 /third라면, views에 있는 third함수의 return 값을 출력해준다.
    path('/third', views.third)
]