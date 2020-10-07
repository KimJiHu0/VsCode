from django.http import HttpResponse

def index(request):
    # first Page라는 문구를 클릭하면 second라는 값을 넘겨주게 된다.
    return HttpResponse('<h1><a href="second">First Page</a></h1>')