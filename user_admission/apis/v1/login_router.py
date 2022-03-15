from django.http import HttpRequest
from django.shortcuts import HttpResponse, render
from ninja import Router

from user_admission.apis.v1.schemas.login_response import LoginResponse

account = Router(tags=["MemberManagement"])


# login page render router
@account.get("/", response=LoginResponse)
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")

