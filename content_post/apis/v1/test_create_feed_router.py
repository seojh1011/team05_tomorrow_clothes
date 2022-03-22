from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import File, Router
from ninja.files import UploadedFile

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.services.get_feed_list_service import create_feed

content = Router(tags=["Content_CRUD"])


# main page render router
# 테스트로 게시글 생성해주는 서비스
@content.post("test/post/", response=MainResponse)
def create_post_page(
    request: HttpRequest, email: str, comment: str, img: UploadedFile = File(...)
) -> HttpResponse:
    a = request.POST
    print(a)
    create_feed(email, comment, img)

    return redirect("/")
