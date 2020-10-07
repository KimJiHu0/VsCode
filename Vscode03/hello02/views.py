# 
from django.shortcuts import render

# Create your views here.
def hello(request):
    # request를 받아서 hello02를 응답해줄건데, data는 name이라는 이름으로 Django를 전달
    return render(request, 'hello02.html', {'name' : 'Django'})
    # 작성 후에 hello에 있는 setting.py에서 'DIRS': [os.path.join(BASE_DIR, 'templates')], 설정

# list로 보내기
def variable01(request):
    lst = ['Python', 'Django', 'Templates']
    return render(request, 'variable01.html', {'list' : lst})

# dct형식(딕셔너리)로 보내기
def variable02(request):
    dct = {'class':'qclass', 'name':'JiHu'}
    return render(request, 'variable02.html', {'dct' : dct})

def forLoop(request):
    return render(request, 'for.html', {'number': range(1,10)})

def if01(request):
    return render(request, 'if01.html', {'user':{ 'id':'qclass', 'name':'JiHu' }})

def if02(request):
    return render(request, 'if02.html', {'role':'manager'})

def href(request):
    return render(request, 'href.html')