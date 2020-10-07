from django.shortcuts import render
from django.http import HttpResponse
from dbtest.models import MyBoard

def index(request):
    return render(request, 'index.html', {'list' : MyBoard.objects.all()})