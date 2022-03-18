from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.shortcuts import HttpResponse, render
from django.http import HttpRequest
from ninja import Router
from user_admission.apis.v1.schemas.logout_response import LogoutResponse

account = Router(tags=["MemberManagement"])

@account.get("/", url_name='logout', response=LogoutResponse)
def get_logout_page(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect('/')

