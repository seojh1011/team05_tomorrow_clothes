from ninja.orm import create_schema

from content_post.models.contents import Feeds

DetailRequest = create_schema(Feeds, fields=["feeds_comment", "feeds_img_url"])
