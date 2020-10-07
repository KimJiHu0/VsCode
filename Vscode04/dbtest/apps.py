from django.apps import AppConfig

# dbtest라는 project안에 dbtest라는 app이 존재하고 후에 또 다른 app이 만들어질텐데
# 이를 설정해주는 apps.py파일 -> 후에 project에서 settings에서 추가해줘야함
class DbtestConfig(AppConfig):
    name = 'dbtest'