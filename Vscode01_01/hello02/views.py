from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello02(request):
    # 아래의 a태그를 클릭하게 되면 hello01/test라는 값이 요청된다.
    # 현재 hello01안에서 만들어져있기 때문에 hello01이 붙어여한다.
    # 뒤에 있는 a태그는 가장 처음화면으로 돌아가는 것인데 href에 /만 적어주면 가장 처음 화면으로 돌아간다.
    return HttpResponse('<h1><a href="hello01/test">Hi, DjangoApp</a></h1> <h1><a href="/">Go hello01</a></h1>')

def test(request):
    return HttpResponse('<h1><a href="/hello01">Test Page</a></h1>')