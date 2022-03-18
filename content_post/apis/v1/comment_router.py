from django.contrib import auth
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from ninja import Router, Form

from content_post.models import Feeds, Comments

content = Router(tags=["Content_CRUD"])


@content.post("/reple/{comment_id}/")
def Write_Reple(request: HttpRequest, comment_id: int, comment:str =Form(...)) -> HttpResponse:
    #로그인을 위한부분
    username = 'seo'
    password = '123'
    me = auth.authenticate(request, username=username, password=password)
    if me is not None:
        auth.login(request, me)
        #로그인을위한 부분
        if request.user.is_authenticated:
            # 로그인했는지 확인
            comment_writer_id = request.user.id
            #로그인한유저의 아이디 = 코멘트 작성자의 아이디
            comment_num_id = Comments.objects.get(id=comment_id).id
            #리플은 댓글의 아이디를 포린키로 받는다
            comment = comment
            #폼에서 코멘트 내용을 받아온다
            feed_id = Comments.objects.get(id=comment_id).feed_id
            #어떤게시물의 댓글인지 피드 아이디에 저장
            Comments.objects.create(
                comment=comment, step='1', comment_writer_id=comment_writer_id, feed_id=feed_id,
                comment_num_id=comment_num_id
            )
            # 코멘트 오브젝트 생성
            feed_id=feed_id.id
            return redirect(f'/detail/{feed_id}/')
        else:
            return redirect('/login/')


@content.post("/{feed_id}/")
def Write_Comment(request: HttpRequest, feed_id: int, comment:str=Form(...)) -> HttpResponse:
    #로그인을위한 부분
    username = 'tester1234'
    password = '1234'
    me = auth.authenticate(request, username=username, password=password)
    if me is not None:
        auth.login(request, me)
        #로그인을 위한 부분
        if request.user.is_authenticated:
            #로그인됐다면
            comment = comment
            #폼으로 코멘트를 받아온다
            comment_writer_id = request.user.id
            #로그인한 유저 = 댓글 작성자
            feed_id = Feeds.objects.get(id=feed_id)
            #어떤 피드의 댓글인지 포린키로 저장
            Comments.objects.create(comment=comment, step=0, feed_id=feed_id, comment_writer_id=comment_writer_id)
            #코멘트 생성
            feed_id=feed_id.id
            return redirect(f'/detail/{feed_id}/')
        else:
            return redirect('/login/')
