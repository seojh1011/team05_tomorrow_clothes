from typing import Any, Dict, List

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from ninja import File, Form, Router, UploadedFile, Schema

from content_post.apis.v1.schemas.detail_response import CommentResponse, DetailResponse, FeedSchema
from content_post.apis.v1.schemas.schema_test import UserSchema
from content_post.models.contents import Comments, Feeds
from user_admission.models.user import User

content = Router(tags=["Feeds_CRUD"])


# detail/feeds page render router
@content.get("/feed/", response=DetailResponse)
@login_required(login_url="/login/")
def get_feed_page(request: HttpRequest) -> HttpResponse:
    return render(request, "add.html")




# # 수정페이지 이동 변경예정 효정님 _______________


# detail/feeds/ (추가)
@content.post("/feed/", response=DetailResponse)
@login_required(login_url="/login/")
def post_feed(
        request: HttpRequest,
        feeds_comment: str = Form(...),
        feeds_img_url: UploadedFile = File(...),
) -> HttpResponse:
    writer = get_object_or_404(User, id=request.user.id)
    Feeds.objects.create(
        feeds_comment=feeds_comment, feeds_img_url=feeds_img_url, writer=writer
    )
    feed_id = Feeds.objects.order_by("-id")[0].id
    return redirect("/detail/" + str(feed_id) + "/")


@content.get("/feed/update/{feed_id}/", response=FeedSchema)
@login_required(login_url="/login/")
def get_update_feed_page(request: HttpRequest, feed_id: int):
    user_id = request.user.id
    feed_writer = Feeds.objects.get(id=feed_id).writer.id
    if user_id == feed_writer:
        feed = Feeds.objects.get(id=feed_id)
        return render(request, 'add.html', {'feed': feed})
    else:
        return redirect(f"/detail/{feed_id}/", {'error': '본인이 작성한 게시물이 아닙니다.'})


@content.get("/feed/update/{feed_id}/", response=FeedSchema)
@login_required(login_url="/login/")
def get_update_feed_page(request: HttpRequest, feed_id: int):
    user_id = request.user.id
    feed_writer = Feeds.objects.get(id=feed_id).writer.id
    if user_id == feed_writer:
        feed = Feeds.objects.get(id=feed_id)
        return render(request, 'add.html', {'feed': feed})
    else:
        return redirect(f"/detail/{feed_id}/", {'error': '본인이 작성한 게시물이 아닙니다.'})


# detail/feeds/<int:feed_id> 수정
@content.post("/feed/update/{feed_id}/")
def update_feed(
        request: HttpRequest,
        feed_id: int,
        feeds_comment: str = Form(...)
) -> Dict[str, str]:
    update_file = request.FILES
    new_feed = Feeds.objects.get(id=feed_id)  # type:ignore
    new_feed.feeds_comment = feeds_comment
    if len(update_file) <= 0:
        new_feed.save()
        return redirect(f"/detail/{feed_id}/")
    else:
        print(update_file['feeds_img_url'])
        new_feed.feeds_img_url = update_file['feeds_img_url']
        new_feed.save()
        return redirect(f"/detail/{feed_id}/")


class Delete1(Schema):
    abc: str


# detail/feeds/<int:feed_id> 삭제
@content.post("/feed/delete/{feed_id}", response=Delete1)
def delete_feed(request: HttpRequest, feed_id: int) -> Dict[str,str]:
    user = request.user
    delete_feed = Feeds.objects.get(id=feed_id)
    delete_feed_user = delete_feed.writer
    if user == delete_feed_user:
        delete_feed.delete()
        return {'abc': '삭제 완료'}
    else:
        return {'abc': '본인이 작성한 글이 아닙니다.'}

# 수정페이지 이동 변경예정

# 상세 FEED페이지로 이동
@content.get("/{feed_id}/", response=List[DetailResponse])
def get_detail_page(request: HttpRequest, feed_id: int) -> HttpResponse:
    user_id = request.user.id
    # 로그인된 유저의 아이디값
    print('스타트')
    try:
        feed = Feeds.objects.get(id=feed_id)
        # 디테일 페이지에 뿌려질 피드 객체
        check = feed.scrape.filter(id=user_id)  # type: ignore
        # 로그인된 유저의 값으로 피드에 스크랩했는지 체크
        comments = Comments.objects.filter(feed_id=feed_id).order_by("-created_at")
        print('시작')
        # 피드에 달린 댓글 객체들
        if check.exists():
            # 만약 스크랩을 했다면
            print('이프')
            return render(
                request,
                "detail.html",
                {"feed": feed, "comments": comments, "scraped": "scraped"},
            )
        else:
            print('엘스')
            # 스크랩을 안했다면
            return render(request, "detail.html", {"feed": feed, "comments": comments})
    except ValueError:
        return redirect('/')
    except TypeError:
        return redirect('/')
    except:
        return redirect('/')
