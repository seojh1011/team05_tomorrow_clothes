from typing import Any, Union

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.services.get_feed_list_service import get_feed_list

content = Router(tags=["Content_CRUD"])


# 김윤서
# main page render router
@content.get("", url_name="main", response=list[MainResponse])
def get_main_page(request: HttpRequest) -> HttpResponse:
    # 가져올 페이지와 리스트 갯수
    page: int = 1
    limit: int = 10
    # 무한 스크롤했을때 get에 리스트가 있으면 실행
    if len(request.GET) > 0:

        page = request.GET["page"]  # type: ignore
        limit = request.GET["limit"]  # type: ignore
        # FEED 객체 불러오는 서비스(n번째 페이지, 가져올 갯수)
        pages = get_feed_list(page, limit)

        if pages is None:
            return list()
        return list(pages)

    # print(limit)
    pages = get_feed_list(page, limit)
    return render(request, "main.html", {"pages": pages})
