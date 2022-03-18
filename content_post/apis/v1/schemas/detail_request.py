from ninja.orm import create_schema
from content_post.models import Feeds


DetailRequest = create_schema(Feeds, fields=['feeds_comment', 'feeds_img_url'])
