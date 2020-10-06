# django에 urls에서 path를 import + include
from django.urls import path, include
# views를 import
from . import views

urlpatterns = [
    # 이름은 hello02고, views에 hello02를
    # 페이지가 켜질 때 가장 먼저 나오는 곳으로 지정한다. 
    path('', views.hello02, name='hello2'),

    # Hi, DjangoApp를 클릭해서 넘어온 값 /test를 받아서 어떤 화면을 보여줄지 지정한다.
    path('/test', views.test),
]