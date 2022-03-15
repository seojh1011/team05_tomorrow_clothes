from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from ninja import Router

from user_admission.apis.v1.schemas.login_response import LoginResponse

login = Router(tags=["MemberManagement"])


# login page render router
@login.get("/", response=LoginResponse)
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")

# 경로가 ~ login/ 이고(/다음에 아무것도 없을때) get이면 위의 함수를 실행해라