from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from ninja import Form, Router

from content_post.models.contents import Comments, Feeds
from content_post.services.comment_service import write_comment, write_reple, comment_update

content = Router(tags=["Comment_crud"])


@content.post("/reple/{comment_id}/")
@login_required(login_url="/login/")
def post_reple(request: HttpRequest, comment_id: int, comment: str = Form(...)) -> HttpResponse:
    comment_writer_id: int = request.user.id  # type: ignore
    # 로그인한유저의 아이디 = 코멘트 작성자의 아이디
    feed_id = write_reple(comment_writer_id, comment_id, comment)
    return redirect(f"/detail/{feed_id}/")


@content.post("/reple/update/{comment_id}/")
@login_required(login_url="/login/")
def update_reple(request: HttpRequest, comment_id: int, comment: str) -> HttpResponse:
    # 로그인했는지 확인
    login_user = request.user.id  # type: ignore
    reple_writer = Comments.objects.get(id=comment_id).comment_writer.id
    if login_user == reple_writer:
        comment_update(comment, comment_id)
        msg = {'success': comment}
        return msg
    else:
        msg = {'error': '본인이 작성한 코멘트가 아닙니다.'}
        return msg


@content.post("/reple/delete/{comment_id}/")
@login_required(login_url="/login/")
def delete_reple(request: HttpRequest, comment_id: int) -> HttpResponse:
    login_user = request.user.id  # type: ignore
    reple_writer = Comments.objects.get(id=comment_id).comment_writer.id
    if login_user == reple_writer:
        # 로그인한 유저 = 댓글 작성자
        delete_comment = Comments.objects.get(id=comment_id)
        # 삭제할 코멘트를 가져와서
        delete_comment.delete()
        # 삭제한다
        msg = {'success': '삭제 완료'}
        # 성공메세지보내기
        return msg
    else:
        msg = {'error': '본인이 작성한 코멘트가 아닙니다.'}
        return msg


@content.post("/{feed_id}/")
@login_required(login_url="/login/")
def post_comment(
        request: HttpRequest, feed_id: int, comment: str = Form(...)
) -> HttpResponse:
    # 폼으로 코멘트를 받아온다
    comment_writer_id: int = request.user.id  # type: ignore
    # 로그인한 유저 = 댓글 작성자
    write_comment(comment_writer_id, feed_id, comment)
    return redirect(f"/detail/{feed_id}/")


@content.post("/update/{comment_id}/")
@login_required(login_url="/login/")
def update_comment(request: HttpRequest, comment_id: int, comment: str) -> HttpResponse:
    login_user = request.user.id  # type: ignore
    comment_writer = Comments.objects.get(id=comment_id).comment_writer.id
    if login_user == comment_writer:
        # 로그인한 유저 = 댓글 작성자가 맞는지 확인
        comment_update(comment, comment_id)
        msg = {'success': comment}
        return msg
    else:
        msg = {'error': '본인이 작성한 코멘트가 아닙니다.'}
        return msg


@content.post("/delete/{comment_id}/")
@login_required(login_url="/login/")
def delete_comment(request: HttpRequest, comment_id: int) -> HttpResponse:
    # 폼으로 코멘트를 받아온다
    login_user = request.user.id  # type: ignore
    comment_writer = Comments.objects.get(id=comment_id).comment_writer_id
    if login_user == comment_writer:
        # 로그인한 유저 = 댓글 작성자
        comment_delete = Comments.objects.get(id=comment_id)
        # 삭제할 코멘트를 가져와서
        comment_delete.delete()
        # 삭제한다
        msg = {'success': '삭제 완료'}
        # 성공메세지보내기
        return msg
    else:
        msg = {'error': '본인이 작성한 코멘트가 아닙니다.'}
        return msg
