# Django & VsCode

> **Django** : 파이썬으로 만들어진 무료 오픈소스 웹 어플리케이션 프레임워크.
> 쉽고 빠르게 웹사이트를 개발할 수 있도록 돕는 구성요소로 이루어져 있다.
>
> 
> 
>
> ### pyweb 가상환경 들어가는 방법
>
> 1. Vscode를 킨 후에 상단에 '**터미널**' 메뉴를 선택한 후에 '**새 터미널 열기**'를 클릭한다.
> 2. '**cmd**'를 선택한 후에 '**cd /**'를 쳐서 가상 최상위 경로로 온다.
> 3. 그 후에 '**cd venvs**'를 치고 경로에 들어온 다음, '**.\pyweb\Scripts\activate.bat**'을 친 다음에 가상환경에 들어온다.
> 4. 다시 '**cd /**'를 친 후에 내가 지정해 놓은 경로로 들어간다.
>    **[ex] cd Workspace/Workspace_Django**
>
> ### 새로운 project를 만들고 안에 폴더를 만들고 서버 실행 방법
>
> 1. '**django-admin startproject 폴더명**'을 친다. 새로운 프로젝트가 생성되었다.
> 2. 예를 들어서 hello01이라는 project 폴더명을 만들었다면, '**cd hello01**'을 치고 들어간다.
> 3. 그 후에 '**python manage.py startapp 폴더명**'을 치게 된다면 hello01이라는 project 안에
>    내가 작성한 폴더명이 생성된다.
> 4. 그 다음 서버를 실행하기 위해서는 '**python manage.py runserver**'을 치게되면 localhost주소가 나오고 ctrl + 좌클릭을 하면 해당 주소창이 열리게 된다.