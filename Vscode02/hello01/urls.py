from django.urls import path
from . import views

urlpatterns = [
    # hello01이라는 값으로 요청이 들어와서 이곳 urlpattern으로 들어왔다.
    # 바로 index가 보여지게 했고 index라는 함수의 값을 index라고 지정했다.
    # 그리고 index를 보여줘!
    path('', views.index, name='index'),
    # test라는 url pattern이 들어오면 views가 가진 test를 보여준다.
    path('test', views.test),
]