from django.db import models

from user_admission.models.user import User


class Feeds(models.Model):
    class Meta:
        db_table = "feeds"

    # 수정일자 설정 auto_now
    updated_at = models.DateTimeField(auto_now=True)
    # 생성일자 설정 auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # 코멘트 생성
    feed_comment = models.CharField(max_length=350, null=False)
    #main-img 경로
    feed_img_url = models.FileField(null=False, upload_to="images")
    #작성자 FK
    writer = models.ForeignKey(User, related_name="user_feed", on_delete=models.CASCADE)
    #tags
    style_tag = models.CharField(max_length=50, null=True)
    #스크랩 숫자
    scrape_num = models.IntegerField(null=True)
    #스크랩 N:N
    scrape = models.ManyToManyField(User, related_name='feed_scrapes')

    def __str__(self):
        return self.feed_comment