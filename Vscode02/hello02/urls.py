# django에 urls에서 path를 import
from django.urls import path
# view를 import
from . import views


# urlpatterns 설정
urlpatterns=[
    # 가장 기본으로 들어오는 페이지는 views에 있는 hello라는 함수의 return값.
    path('', views.hello),
]