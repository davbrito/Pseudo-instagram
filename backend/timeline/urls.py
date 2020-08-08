from django.urls import include, path
from rest_framework import routers, viewsets

from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
# router.register(r'comments', views.CommentViewSet)

# app_name = 'timeline'

urlpatterns = [
    path('posts/<int:post_id>/comments/', views.CommentList.as_view()),
    path('posts/<int:post_id>/comments/<int:pk>/',
         views.CommentDetail.as_view()),
    path('', include(router.urls)),
]
