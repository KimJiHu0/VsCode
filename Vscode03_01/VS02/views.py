from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # 현재 이 app. 즉, 페이지가 보여지는 url은 localhost:/second 에서 보여지는 화면이다.
    # 그래서 요청값을 second/third를 보내주게 되면 urls.py에서 요청을 처리하게 된다.
    return HttpResponse('<h1><a href="second/third">Second Page</a></h1>')

def third(request):
    # 이 Third Page를 클릭하면 가장 최상위 값을 불러와서 First Page가 출력된다.
    return HttpResponse('<h1><a href="/">Third Page</a></h1>')
