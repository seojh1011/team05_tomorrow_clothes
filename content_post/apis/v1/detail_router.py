from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.detail_response import DetailResponse

content = Router(tags=["Content_CRUD"])


# detail page render router
@content.get("", response=DetailResponse)
def get_detail_page(request: HttpRequest) -> HttpResponse:
    return render(request, "detail.html")


# detail/feeds page render router
@content.get("/feeds/", response=DetailResponse)
def get_feeds_page(request: HttpRequest) -> HttpResponse:
    return render(request, "add.html")


# # 수정페이지 이동 변경예정
# @detail.get('/feeds/', response=DetailResponse)
# def get_update_page(request: HttpRequest):
#     return render(request, 'add.html')
