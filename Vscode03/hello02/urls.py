# django에 urls에서 path를 import
from django.urls import path
# view를 import
from . import views


# urlpatterns 설정
urlpatterns=[
    # 가장 기본으로 들어오는 페이지는 views에 있는 hello라는 함수의 return값.
    # name을 index로 지정했다.
    path('', views.hello, name='index'),
    path('var01', views.variable01),
    path('var02', views.variable02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
    path('href', views.href),
]