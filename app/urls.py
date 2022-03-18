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
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI


from user_admission import views
from content_post.apis.v1.comment_router import content as comment_router
from content_post.apis.v1.detail_router import content as detail_router
from content_post.apis.v1.main_router import content as main_router
from user_admission.apis.v1.login_router import account as login_router
from user_admission.apis.v1.register_router import account as register_router
from user_admission.apis.v1.logout_router import account as logout_router

api = NinjaAPI(version="1.0.0", urls_namespace="test_1")
api.add_router("/login/", login_router)
api.add_router("/logout/", logout_router)
api.add_router("/register/", register_router)
api.add_router("/", main_router)
api.add_router("/detail/", detail_router)
api.add_router("/comment/", comment_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", api.urls),
    # path('', include('user_admission.urls')),
    # path('', include('content_post.urls')),
    path('join/', views.create_user, name="create_user")

]
