"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, reverse
from ninja import NinjaAPI

from app import settings
from content_post.apis.v1.detail_router import content as detail_router
from content_post.apis.v1.main_router import content as main_router
from user_admission.apis.v1.login_router import account as login_router
from user_admission.apis.v1.register_router import account as register_router
from content_post.apis.v1.create_feed_router import content as create_router

api = NinjaAPI()
api.add_router("login", login_router)
api.add_router("/register/", register_router)
api.add_router("/", main_router)
api.add_router("/detail/", detail_router)
api.add_router("/", create_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
    # path('', include('user_admission.urls')),
    # path('', include('content_post.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


reverse('api-1.0.0:login')