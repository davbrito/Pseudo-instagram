from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)

comment_router = routers.DefaultRouter()
comment_router.register(r'comments', views.CommentViewSet)
# router.register(r'comments', views.CommentViewSet)

# app_name = 'timeline'

urlpatterns = [
    # path('posts/<int:post_id>/comments/',
    #      views.CommentViewSet.as_view({
    #          'get': 'list',
    #          'post': 'create'
    #      })),
    # path(
    #     'posts/<int:post_id>/comments/<int:pk>/',
    #     views.CommentViewSet.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'patch': 'partial_update',
    #         'delete': 'destroy'
    #     })),
    path('', include(router.urls)),
    re_path(r'(posts/(?P<post_id>\d+)/)?', include(comment_router.urls)),
]
