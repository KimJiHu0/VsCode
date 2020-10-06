from django.urls import path
from . import views

# 가장먼저 켜지는 메인이 views에 있는 hello라는 함수의 리턴값이다.
urlpatterns=[
    path('', views.hello),
]