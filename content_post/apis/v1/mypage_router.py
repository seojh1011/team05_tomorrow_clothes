from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router, UploadedFile, Form

from content_post.models import Feeds
from user_admission.models import User

content = Router(tags=["MyPage"])



@content.get("/")
def get_my_page(request: HttpRequest) -> HttpResponse:
    user_id = '18'
    # user_id = request.user.id
    user_information = User.objects.get(id=user_id)
    user_feeds = Feeds.objects.filter(writer_id=user_id)
    scrap_feeds = Feeds.objects.filter(scrape=user_id)
    return render(request, 'add.html',
                  {'user_information': user_information, 'user_feeds': user_feeds, 'scrap_feeds': scrap_feeds})


@content.get("/user/")
def get_my_user_page(request: HttpRequest) -> HttpResponse:
    return render(request, "mypage.html")


@content.get("/user/profile/")
def get_my_user_page(request: HttpRequest) -> HttpResponse:
    return render(request, "profile.html")


@content.get("/update/")
def get_update_profile_page(request: HttpRequest):
    user_id = '16'
    user = User.objects.get(id=user_id)
    # user = request.user
    pro_img_url = user.feeds_img_url
    nick_name = user.nick_name
    return render(request, 'add.html', {'pro_img_url': pro_img_url, 'nick_name': nick_name})


@content.post("/update/")
def update_profile(request: HttpRequest, nick_name: str = Form(...)) -> Dict:
    user_id = '16'
    user = User.objects.get(id=user_id)
    # user = request.user
    user.nick_name = nick_name
    update_file = request.FILES
    if len(update_file) <= 0:
        user.save()
        return {'success': '프로필 업데이트 완료'}
    else:
        user.pro_img_url = update_file['feeds_img_url']
        return {'success': '프로필 업데이트 완료'}
