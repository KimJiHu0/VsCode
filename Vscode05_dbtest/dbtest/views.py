from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from dbtest.models import MyBoard
# sysdate를 insert하기 위해서는 timezone.now()를 써야해서 import
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {'list' : MyBoard.objects.all()})

# id라는 값은 Django가 알아서 만들어준다.
# 상세보기 가는 함수
def detail(request, id):
    return render(request, 'detail.html', {'dto' : MyBoard.objects.get(id=id)})

# 수정 폼으로 가는 함수
def updateform(request, id):
    return render(request, 'update.html', {'dto' : MyBoard.objects.get(id=id)})

# 수정하는 함수
def updateres(request):
    # request.getParameter('id') 식으로 받아준 것이다.

    # post방식으로 넘어온 id, mytitle, mycontent를 각각의 이름으로 담아준다.
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    # MyBoard에서 id가 id인애들만 걸러서 가져온다
    myboard = MyBoard.objects.filter(id=id)
    # resultTitle, resultContent에다가 가져온 myboard에서 update해주는데 mytitle과 mycontent를 update해준다.
    resultTitle = myboard.update(mytitle = mytitle)
    resultContent = myboard.update(mycontent = mycontent)

    # 성공한 결과값이 각각 1이 나오기 때문에 1+1은 2. 즉, 두개 다 성공했다면
    if resultTitle + resultContent == 2:
        # 아래의 경로로
        return redirect('detail/'+id)
    # update에 실패했다면
    else:
        # 아래의 경로로
        return redirect('updateform/'+id)

# 삭제하는 함수
def delete(request, id):
    # MyBoard.objects.filter(id=id) : id가 id인 애들만 걸러서 찾아온다.
    # .delete() : 삭제해줘라 그리고 resultDelete에 담아라
    resultDelete = MyBoard.objects.filter(id=id).delete()

    # delete는 tuple로 담긴다?결과창 확인해보면 될듯. 왜 resultDelete[]라고 했는지
    print("delete result : ", resultDelete)


    if resultDelete[0] == 1:
        return redirect('index')
    else:
        return redirect('detail/' + id)

# insertform가는 함수
def insertform(request):
    return render(request, 'insert.html')

# insert 결과 처리해주는 함수
def insertres(request):
    
    # insertform에서 form태그로 post방식으로 전해준 myname, mytitle, mycontent를 받아준다.
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    # 그리고 result라는 변수에 받아오 애들과 현재시간을 create()를 통해 insert해준다.
    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())

    # 이 말은 result : 과 같은 의미이고 성공한다면, 
    if result:
        # index로 가라
        return redirect('index')
    # 실패했다면
    else:
        # insertform으로 가라.
        return redirect('insertform')
