from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from ninja import Router

from user_admission.apis.v1.schemas.login_response import LoginResponse

login = Router()


# login page render router
@login.get("/", response=LoginResponse)
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")
