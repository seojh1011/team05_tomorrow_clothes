from django.db import models

from user_admission.models import User


class Feeds(models.Model):
    class Meta:
        db_table = "FEED"

    # 생성일자 설정 auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일자 설정 auto_now
    updated_at = models.DateTimeField(auto_now=True)
    # 코멘트 생성
    feeds_comment = models.TextField()
    # main-img 경로
    # feeds_img_url = models.FileField(upload_to="images", blank=True, null=True)
    feeds_img_url = models.ImageField(upload_to="images/", blank=True, null=True)
    # 작성자 FK
    writer = models.ForeignKey(User, related_name="user_feed", on_delete=models.CASCADE)
    # tags
    style_tag = models.CharField(max_length=100, null=True)
    # 스크랩 N:N
    scrape = models.ManyToManyField(User)
    # 스크랩 숫자
    scrapes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = "COMMENT"

    # 참조하는 게시글
    feed_id = models.ForeignKey(
        Feeds,
        related_name="feed_comment",
        db_column="feed_id",
        on_delete=models.CASCADE,
    )
    # 코멘트
    comment = models.TextField()
    # 코멘트 작성자
    comment_writer = models.ForeignKey(
        User, related_name="user_comment", on_delete=models.CASCADE
    )
    # 코멘트의 단계 0 >>코멘트, 1>>코멘트의 답글
    step = models.IntegerField(default=0)
    # 참조하는 코멘트 (대댓글이 어떤 코멘트의 자식인가)
    comment_num = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    # 생성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정일
    updated_at = models.DateTimeField(auto_now=True)
