# 
from django.shortcuts import render

# Create your views here.
def hello(request):
    # request를 받아서 hello02를 응답해줄건데, data는 name이라는 이름으로 Django를 전달
    return render(request, 'hello02.html', {'name' : 'Django'})
    # 작성 후에 hello에 있는 setting.py에서 'DIRS': [os.path.join(BASE_DIR, 'templates')], 설정

def variable01(request):
    lst = ['Python', 'Django', 'Templates']
    return render(request, 'variable01.html', {'list' : lst})