from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.models import Feeds
from django.core.paginator import Paginator # 삭제필요

content = Router(tags=["Content_CRUD"])


# main page render router
@content.get("", response=MainResponse)
def get_main_page(request: HttpRequest) -> HttpResponse:
    page_list = Paginator(Feeds.objects.order_by("-id"), 10).page(1)
    return render(request, "main.html", {"test": page_list})
