from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register('posts', PostViewSet, basename='posts')
api_v1_router.register('groups', GroupViewSet, basename='groups')
api_v1_router.register('follow', FollowViewSet, basename='follow')
api_v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                       CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
    path('auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
