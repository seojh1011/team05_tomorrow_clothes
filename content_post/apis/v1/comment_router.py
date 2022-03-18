from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from ninja import Form, Router

from typing import Optional, Union, Any
from django.db.models import BigAutoField


from content_post.models.contents import Comments, Feeds

content = Router(tags=["Content_CRUD"])


@content.post("/reple/{comment_id}/")
@login_required(login_url="/login/")
def Write_Reple(
        request: HttpRequest, comment_id: int, comments: str = Form(...)
) -> HttpResponse:
    # 로그인했는지 확인
    # comment_writer_id: Optional[int] = None
    comment_writer_id: int = request.user.id # type: ignore
    # 로그인한유저의 아이디 = 코멘트 작성자의 아이디
    comment_num_id: int = Comments.objects.get(id=comment_id).id
    # 리플은 댓글의 아이디를 포린키로 받는다
    comment: str = comments
    # 폼에서 코멘트 내용을 받아온다
    feed_num: Feeds = Comments.objects.get(id=comment_id).feed_id
    # 어떤게시물의 댓글인지 피드 아이디에 저장
    Comments.objects.create(
        comment=comment,
        step="1",
        comment_writer_id=comment_writer_id,
        feed_id=feed_num,
        comment_num_id=comment_num_id,
    )
    # 코멘트 오브젝트 생성
    feed_id: int = feed_num.id
    return redirect(f"/detail/{feed_id}/")


@content.post("/{feed_id}/")
@login_required(login_url="/login/")
def Write_Comment(
        request: HttpRequest, feed_id: int, comment: str = Form(...)
) -> HttpResponse:
    # 폼으로 코멘트를 받아온다
    comment_writer_id: int = request.user.id # type: ignore
    # 로그인한 유저 = 댓글 작성자
    feed_num: Feeds = Feeds.objects.get(id=feed_id)
    # 어떤 피드의 댓글인지 포린키로 저장
    Comments.objects.create(
        comment=comment, step=0, feed_id=feed_num, comment_writer_id=comment_writer_id
    )
    # 코멘트 생성
    feed_id = feed_num.id
    return redirect(f"/detail/{feed_id}/")
