from django.shortcuts import render

# Create your views here.
def htmlpage(request):
    return render(request, 'index.html', {'name':'이름'})

# list에 값 담아서 보낸기.
def htmllist(request):
    # lst라는 이름으로 값을 배열로 담는다.
    lst = ['First List','Second List','Third List']
    # 배열을 담은 변수 lst를 list라는 이름으로 담아 보낸다.
    return render(request, 'list.html', {'list' : lst})

# dictionary 형태로 값 담아서 보내기
def htmldct(request):
    # dictionary형태를 dct라는 이름으로 담았다.
    dct = {'name' : 'Name dct', 'class' : 'Class dct'}
    # dct라는 이름으로 dct를 담아서 dct.html를 보여줄것이다.
    return render(request, 'dct.html', {'dct' : dct})

# html에서 반복문을 돌리기 위해서 값 보내기
def htmlfor(request):
    # number라는 이름으로 1부터 10까지를 넣어서 for.html를 보여줄건데 같이 넘겨줄거다.
    return render(request, 'for.html', {'number' : range(1,10)})

# if문을 위해 값 보내기 if
def htmlif01(request):
    return render(request, 'if01.html', {'user' : {'id' : 'Id First', 'name' : 'Name Second'}})

# if문을 위해 값 보낸기 if / else if / else
def htmlif02(request):
    # role이라는 것에 manager를 담아서 if02.html를 보여줄 때 값을 같이 보내준다.
    return render(request, 'if02.html', {'role' : 'manager'})

# href하는 방법을 보여주기 위한 함수.
def htmlhref(request):
    return render(request, 'href.html')
