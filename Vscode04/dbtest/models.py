from django.db import models

# python manage.py makemigrations dbtest 명령어란?
# dbtest라는 project에서 models.py에서 model을 만들어주었는데 이를 생성해주는 명령어

# java에서 sql파일에서 table만드는 것과 동일
class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateField('date published')
