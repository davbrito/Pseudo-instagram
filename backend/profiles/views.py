from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .permissions import IsUserOrReadOnly
from .serializers import ProfileSerializer, UserSerializer

# class ProfileViewSet(ModelViewSet):
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    lookup_field = 'username'

    @action(methods=['get', 'put', 'patch'],
            detail=True,
            url_path='profile',
            lookup_field='user__username',
            lookup_url_kwarg='username',
            queryset=Profile.objects.all(),
            serializer_class=ProfileSerializer,
            permission_classes=[
                permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly
            ])
    def profile(self, request: Request, username=None):
        if request.method == 'GET':
            return self.retrieve(request)
        if request.method == 'PUT':
            return self.update(request)
        if request.method == 'PATCH':
            return self.partial_update(request)

    @action(detail=True,
            methods=['get'],
            url_path='profile/follow',
            permission_classes=[permissions.IsAuthenticated])
    def follow(self, request: Request, username=None):
        try:
            this_profile = self.get_object().profile
            request_profile = request.user.profile
            if this_profile == request_profile:
                raise ValidationError('you can´t follow yourself')
            request_profile.followed.add(this_profile)
            return Response(status=status.HTTP_201_CREATED)
        except User.profile.RelatedObjectDoesNotExist as e:
            raise NotFound(detail='This user doesn´t have a profile to follow')

    @action(detail=True,
            methods=['get'],
            url_path='profile/followers',
            serializer_class=UserSerializer
            # ,
            # lookup_field='profile',
            # lookup_url_kwarg='username'
            )
    def profile_followers(self, request: Request, username=None):
        return self._list_queryset(
            User.objects.filter(profile__followed__user=self.get_object()))

    @action(detail=True,
            methods=['get'],
            url_path='profile/followed',
            serializer_class=UserSerializer)
    def profile_followed(self, request: Request, username=None):
        return self._list_queryset(
            User.objects.filter(profile__followers=self.get_object().profile))

    def _list_queryset(self, queryset):
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
