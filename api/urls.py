from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>[0-9]+)/comments', views.CommentViewSet, basename='comments')
router.register('follow', views.FollowViewSet, basename='follows')
router.register('group', views.GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]