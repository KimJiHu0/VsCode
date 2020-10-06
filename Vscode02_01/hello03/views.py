from django.shortcuts import render

# Create your views here.
def hello(request):
    # request를 받아서 hello02.html를 보여주는데 name이라는 이름에 KimJiHu라는 값을 넣어준 후 보내준다.
    return render(request, 'hello02.html', {'name':'KimJiHu'})