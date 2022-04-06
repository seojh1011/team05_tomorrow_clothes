from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from ninja import Router, Form

from user_admission.apis.v1.schemas.login_response import LoginResponse
from user_admission.apis.v1.schemas.login_request import LoginRequest

account = Router(tags=["MemberManagement"])


# login page render router

# @account.get("/", response=LoginResponse)
# def get_login_page(request: HttpRequest) -> HttpResponse:
#     return render(request, "login.html")

# 경로가 ~ login/ 이고(/다음에 아무것도 없을때) get이면 위의 함수를 실행해라


@account.get("/", url_name="login", response=LoginResponse)
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")


@account.post("/", url_name="login", response=LoginResponse)
def post_login(request: HttpRequest,loginrequest:LoginRequest = Form(...)) -> HttpResponse:
    # username = request.POST["username"]
    # password = request.POST["password"]
    username = loginrequest.username
    password = loginrequest.password
    user = auth.authenticate(request, username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect("/")
    else:
        error = {"error": "이메일 또는 비밀번호를 확인해주세요."}
        return render(request,"login.html",error)
