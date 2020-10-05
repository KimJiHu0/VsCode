from django.http import HttpResponse

def index(request):
    # a태그로 hello01이라는 값을 요청했다.
    return HttpResponse('<h1><a href="/hello01">Hello, Django!</a></h1>')