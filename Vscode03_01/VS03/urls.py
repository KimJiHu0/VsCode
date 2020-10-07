from django.urls import path
from . import views

urlpatterns=[
    # VS03의 urls로 들어왔을 때 가장 먼저 보여지는 페이지는 views에 있는 htmlpage 함수의 return값이다.
    # 이름은 index.
    path('', views.htmlpage, name='index'),
    # /list라고 요청이 들어오면 views에 있는 htmllist 함수의 return값을 실행, 이름은 list
    path('/list', views.htmllist, name='list'),
    # /dct라고 요청이 들어오면 views에 있는 htmldct함수 return값 실행, 이름은 dct
    path('/dct', views.htmldct, name='dct'),
    # /for라고 요청이 들어오면 views에 있는 htmlfor함수 return값 실행, 이름은 for
    path('/for', views.htmlfor, name='for'),
    # /if01, /if02 라고 요청이 들어오면 views에 있는 htmlif01, htmlif02 함수 각각의 return갑 실행, 이름은 if01, if02
    path('/if01', views.htmlif01, name='if01'),
    path('/if02', views.htmlif02, name='if02'),
    # /href라고 요청이 들어오면 views에 있는 htmlhref함수 return값 실행, 이름은 href
    path('/href', views.htmlhref, name='href'),
]