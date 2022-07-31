from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.views import TokenView

from .views import (
    ReviewViewSet,
    CommentViewSet,
    UserViewSet,
    GenreViewSet,
    CategoryViewSet,
    TitleViewSet,
    SignupViewSet,
)

router = DefaultRouter()
router.register(r'v1/users', UserViewSet, basename='users')
router.register(r'v1/auth/signup', SignupViewSet, basename='signup')

router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')

router.register(r'v1/genres', GenreViewSet)
router.register(r'v1/categories', CategoryViewSet)
router.register(r'v1/titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/auth/token/', TokenView.as_view()),
    path('', include(router.urls)),
]
