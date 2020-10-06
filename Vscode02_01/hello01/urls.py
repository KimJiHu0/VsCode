"""hello01 URL Configuration

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
# 원래는 import가 path만 되어있었지만 include를 추가해줬다.
from django.urls import path, include
# view.py에 있는 모든것을 사용하기 위한 import를 해준다.
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 그리고 path를 추가해줘야한다.
    # 앞 부분에 ''의 의미는 페이지가 켜졌을 때,
    # 가장 먼저 들어오는 페이지를 지정해주는 것이라고 볼 수 있고
    # 그 페이지는 views에 있는 hello01이라는 함수의 return 값을 의미힌다.
    path('', views.hello01),
    # 만일 hello01이라는 요청값이 들어오게되면 hello02에 있는 urls에 연결해주라는 의미이다.
    path('hello01', include('hello02.urls')),

    # hello02/ 라는 요청이 들어오면 hello03에 있는 urls와 연결해주라는 의미이다.
    path('hello02/', include('hello03.urls')),
]
