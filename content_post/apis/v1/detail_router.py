from typing import List

from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from ninja import Router, Form, File, UploadedFile

from content_post.apis.v1.schemas.detail_response import DetailResponse, CommentResponse
from content_post.models import Feeds, Comments
from user_admission.models import User

content = Router(tags=["Content_CRUD"])


@content.post("/scrap/{feed_id}/",url_name='scrap')
def scrap(request: HttpRequest, feed_id: int) -> HttpResponse:
    # 여기부터는 로그인을 위해 잠깐 넣었습니다
    username = 'seo'
    password = '123'
    me = auth.authenticate(request, username=username, password=password)
    if me is not None:
        auth.login(request, me)
        # 여기까지는 로그인을위해서
        user_id = request.user.id
        # 로그인한 유저의 정보가져오기
        user = User.objects.get(id=user_id)
        # user = 로그인한 객체
        feed = Feeds.objects.get(id=feed_id)
        # feed = 스크랩할 피드의 객체
        exist_check = feed.scrape.filter(id=user_id)
        #scrape필드에 로그인한 유저가있는지 체크
        if exist_check.exists():
            #만약 있다면
            Feeds.objects.get(id=feed_id).scrape.remove(user)
            #scrape필드에서 유저를 제거
            feed.scrapes -= 1
            #스크랩카운트 -1
            feed.save()
            #저장
            scrap_count = feed.scrapes
            #저장된 스크립카운트
            ajax = {'scrap_count':scrap_count}
            #딕셔너리형태로 제이슨으로 보낸다
            return JsonResponse(ajax)
        else:
            #없다면
            Feeds.objects.get(id=feed_id).scrape.add(user)
            #scrape필드에 유저를 추가
            feed.scrapes += 1
            #스크랩카운트+1
            feed.save()
            #저장
            scrap_count = feed.scrapes
            #저장된카운트
            ajax = {'scrap_count': scrap_count}
            # 딕셔너리형태로 제이슨으로 보낸다
            return JsonResponse(ajax)


@content.delete("/scrap/{feed_id}/")
def scrap_off(request: HttpRequest, feed_id: int, user_id: int) -> HttpResponse:
    Feeds.objects.get(id=feed_id).scrape.remove(User.objects.get(id=user_id))
    return redirect('/')


# detail page render router
@content.get("/{feed_id}/", response=List[DetailResponse])
def get_detail_page(request: HttpRequest, feed_id: int) -> HttpResponse:
    #로그인을위해 잠시 입력
    username = 'seo'
    password = '123'
    me = auth.authenticate(request, username=username, password=password)
    if me is not None:
        auth.login(request, me)
        #로그인을 위해 잠시입력
        user_id = request.user.id
        #로그인된 유저의 아이디값
        feed = Feeds.objects.get(id=feed_id)
        #디테일 페이지에 뿌려질 피드 객체
        check = feed.scrape.filter(id=user_id)
        #로그인된 유저의 값으로 피드에 스크랩했는지 체크
        comments = Comments.objects.filter(feed_id=feed_id).order_by('-created_at')
        #피드에 달린 댓글 객체들
        if check.exists():
            #만약 스크랩을 했다면
            return render(request, "detail.html", {'feed': feed, 'comments': comments,'scraped':'scraped'})
        else:
            #스크랩을 안했다면
            return render(request, "detail.html", {'feed': feed, 'comments': comments})


# detail/feeds
@content.get("/feeds/", response=DetailResponse)
def get_feeds_page(request: HttpRequest) -> HttpResponse:
    return render(request, "add.html")



# detail/feeds/ (추가)
@content.post('/feeds/', response=DetailResponse)
@login_required(login_url='/login/')
def post_feeds_page(request, writer_id: int = 9, feeds_comment: str = Form(...), feeds_img_url: UploadedFile = File(...)):
    writer = get_object_or_404(User, id=writer_id)
    Feeds.objects.create(feeds_comment=feeds_comment, feeds_img_url=feeds_img_url, writer=writer)
    feed_id = Feeds.objects.order_by('-id')[0].id
    return redirect("/detail/feeds/" + str(feed_id) + "/")


# detail/feeds/<int:feed_id> 수정
@content.put('/feeds/{feed_id}/', response=DetailResponse)
def put_feeds_page(request, feed_id: int, feeds_comment: str = Form(...), feeds_img_url: UploadedFile = File(...)):
    new_feed = Feeds.objects.get_object_or_404(Feeds, id=feed_id)
    new_feed.feeds_comment = feeds_comment
    new_feed.feeds_img_url = feeds_img_url
    new_feed.save()
    return redirect("/detail/feeds/" + str(feed_id) + "/")


# detail/feeds/<int:feed_id> 삭제
@content.delete('/feeds/{feed_id}', response=DetailResponse)
def delete_feeds_page(request, feed_id):
    delete_feed = get_object_or_404(Feeds, id=feed_id)
    delete_feed.delete()
    return redirect('/')

  
# 수정페이지 이동 변경예정
# @detail.get('/feeds/', response=DetailResponse)
# def get_update_page(request: HttpRequest):
#     return render(request, 'add.html')