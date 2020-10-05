# 
from django.shortcuts import render

# Create your views here.
def hello(request):
    # request를 받아서 hello02를 응답해줄건데, data는 name이라는 이름으로 Django를 전달
    return render(request, 'hello02.html', {'name' : 'Django'})

