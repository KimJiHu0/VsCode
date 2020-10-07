from django.shortcuts import render
from django.http import HttpResponse

# index라는 함수
def index(request):
    return HttpResponse('<h1><a href="/hello01/test">Hello, DjangoApp</a></h1>')


def test(request):
    return HttpResponse('<h1><a href="/hello01">Test Page</a></h1>')