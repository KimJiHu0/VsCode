"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# . 이라는 것은 나랑 같은 위치에 있는 views를 import
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # '' : 실행했을 때 가장 처음에 나오는 view를 정해주는데 / views라는 module에서 index라는 메소드를
    # 지정해줬다.
    path('', views.index),
    # hello01로 넘어오는 애들은 hello01에 있는 urls랑 연결해주겠다는 의미.
    # views.py에서 a태그로 값이 hello01이 넘어왔고 hello01.urls와 연결해줬다.
    # 그럼 넘어온 값으로 처리가 되는 곳은 hello01.urls에서 처리가 된다.
    path('hello01/', include('hello01.urls')),
]
