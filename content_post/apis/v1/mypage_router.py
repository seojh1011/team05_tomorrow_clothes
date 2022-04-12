from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from ninja import Router, UploadedFile, Form

from content_post.models import Feeds
from user_admission.models import User

content = Router(tags=["MyPage"])



@content.get("/", url_name="mypage")
def get_my_page(request: HttpRequest) -> HttpResponse:
    user_id = request.user.id
    #로그인유저아이디
    user_information = User.objects.get(id=user_id)
    #로그인한유저 정보
    user_feeds = Feeds.objects.filter(writer_id=user_id)
    #유저가 작성한 피드객체
    scrap_feeds = Feeds.objects.filter(scrape=user_id)
    #유저가 스크랩한 피드객체
    return render(request, 'mypage.html',
                  {'user_information': user_information, 'user_feeds': user_feeds, 'scrap_feeds': scrap_feeds})
    #마이페이지로 유저정보, 작성피드, 스크랩피드 객체를 가지고 랜더

@content.get("/profile/")
def get_my_user_page(request: HttpRequest) -> HttpResponse:
    user = request.user
    #로그인한유저
    return render(request, 'profile.html', {'user': user})
    #프로필수정페이지로 이동 유저객체를 가지고


@content.post("/update/")
def update_profile(request: HttpRequest, nick_name: str = Form(...)) -> Dict:
    user = request.user
    #로그인유저 정보
    user.nick_name = nick_name
    #유저닉네임 = 새로 받은 닉네임
    update_file = request.FILES
    #새로받은 프로필이미지
    if len(update_file) <= 0:
        #이미지가 없다면
        user.save()
        #저장
        return redirect('/mypage')
    else:
        user.pro_img_url = update_file['feeds_img_url']
        #유저프로필 = 새로받은 프로필이미지
        user.save()
        #저장
        return redirect('/mypage')
