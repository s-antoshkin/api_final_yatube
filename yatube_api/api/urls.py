from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = "api"

router = DefaultRouter()
router.register("v1/posts", PostViewSet)
router.register(
    r"v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register("v1/follow", FollowViewSet)
router.register("v1/groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
