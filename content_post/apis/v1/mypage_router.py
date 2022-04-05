from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from ninja import Router, UploadedFile, Form

from content_post.models import Feeds
from user_admission.models import User

content = Router(tags=["MyPage"])



@content.get("/")
def get_my_page(request: HttpRequest) -> HttpResponse:
    # user_id = '18'
    user_id = request.user.id
    user_information = User.objects.get(id=user_id)
    user_feeds = Feeds.objects.filter(writer_id=user_id)
    scrap_feeds = Feeds.objects.filter(scrape=user_id)
    return render(request, 'mypage.html',
                  {'user_information': user_information, 'user_feeds': user_feeds, 'scrap_feeds': scrap_feeds})


@content.get("/profile/")
def get_my_user_page(request: HttpRequest) -> HttpResponse:
    user = request.user
    return render(request, 'profile.html', {'user': user})


@content.post("/update/")
def update_profile(request: HttpRequest, nick_name: str = Form(...)) -> Dict:
    user = request.user
    user.nick_name = nick_name
    update_file = request.FILES
    if len(update_file) <= 0:
        user.save()
        return redirect('/mypage')
    else:
        user.pro_img_url = update_file['feeds_img_url']
        user.save()
        return redirect('/mypage')
