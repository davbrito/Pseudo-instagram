from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from _utilities.views import list_queryset

from .models import Profile
from .permissions import IsOwnerOrReadOnly, ReadOnly
from .serializers import ProfileSerializer, UserSerializer

# class ProfileViewSet(ModelViewSet):
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [ReadOnly]

    lookup_field = 'username'

    @action(methods=['get', 'put', 'patch'],
            detail=True,
            url_path='profile',
            lookup_field='user__username',
            lookup_url_kwarg='username',
            queryset=Profile.objects.all(),
            serializer_class=ProfileSerializer,
            permission_classes=[
                permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
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
        this_user = self.get_object()
        try:
            this_profile = this_user.profile
            request_profile = request.user.profile
            if this_profile == request_profile:
                raise ValidationError('you can´t follow yourself')
            request_profile.following.add(this_profile)
            return Response(status=status.HTTP_201_CREATED)
        except User.profile.RelatedObjectDoesNotExist:  # pylint: disable=no-member
            raise NotFound(detail='User %s doesn´t have a profile to follow' %
                           this_user.username)

    @action(detail=True,
            methods=['delete'],
            url_path='profile/unfollow',
            permission_classes=[permissions.IsAuthenticated])
    def unfollow(self, request: Request, username=None):
        self.get_object().profile.following.remove(request.user.profile)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'], url_path='profile/followers')
    def profile_followers(self, request: Request, *, username=None):
        user = self.get_object()
        return list_queryset(
            self,
            # los perfiles que me siguen son mis seguidores
            self.get_queryset().filter(profile__following=user.profile),
        )

    @action(detail=True, methods=['get'], url_path='profile/following')
    def profile_following(self, request: Request, *, username=None):
        user = self.get_object()
        return list_queryset(
            self,
            # los perfiles que me tiene como seguidor son a los que he seguido
            self.get_queryset().filter(profile__followers=user.profile),
        )
