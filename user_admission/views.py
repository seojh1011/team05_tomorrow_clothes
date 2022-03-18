from django.shortcuts import redirect

from user_admission.models.user import User

def create_user(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    nick_name = request.GET.get('nick_name')
    User.objects.create_user(username=username, password=password, nick_name=nick_name)

    return redirect('/login/')

#render는 이미 만들어져 있으니 다시 안쓴다 html페이지를 값으로 준다
#redirect는 주소를 값으로 준다.

#웹페이지 join 경로에서 아래 쿼리문을 작성한다
#http://localhost:8000/join?username=hyeon&password=1234&nick_name=yeong


