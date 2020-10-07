"""VS01 URL Configuration

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
# views를 import
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 가장 처음으로 들어와지는 main view는 views에 있는 index라는 함수 return값이다.
    path('', views.index),
    # 만일 second라는 값으로 요청이 들어온 경우, VS02 app에 있는 urls에게 넘겨준다.
    path('second', include('VS02.urls')),
    # 요청값이 VS03이라고 들어오면 VS03에 있는 urls랑 연결을 해준다.
    path('VS03', include('VS03.urls')),
]
