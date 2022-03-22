from content_post.models import Feeds, Comments


def write_comment(comment_writer_id, feed_id, comment):

    feed_num: Feeds = Feeds.objects.get(id=feed_id)
    # 어떤 피드의 댓글인지 포린키로 저장
    Comments.objects.create(
        comment=comment, step=0, feed_id=feed_num, comment_writer_id=comment_writer_id
    )
    # 코멘트 생성
def update_comment(comment,comment_id):

    Comments.objects.filter(id=comment_id).update(comment=comment)
    # 필터로 댓글객체를 찾아 코멘트를 새로운 코멘트로 수정


def write_reple(comment_writer_id, comment_id, comment):
    comment_num_id: int = Comments.objects.get(id=comment_id).id
    # 리플은 댓글의 아이디를 포린키로 받는다
    comment: str = comment
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
    return feed_id
