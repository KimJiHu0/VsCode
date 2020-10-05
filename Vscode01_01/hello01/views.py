# view.py는 내가 보여줄 화면을 만들어놓는 python file이다.

# 아래와 같이 djanho에 http에서 httpResponse를 import해준다.
from django.http import HttpResponse

# 함수를 선언해준다. 이제 이 함수를 urls.py에서 고쳐줘야한다.
def hello01(request):
    # 아래의 a태그를 클릭하게되면 /hello01이라는 값이 요청되게 된다.
    return HttpResponse('<h1><a href="/hello01">Hi, Django.</a></h1><p>hello01 Method</p>')