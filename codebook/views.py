# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from codebook.models import Language, Post
from codebook.models import User
from codebook.serializers import CommentSerializer, LanguageDetailSerializer, PostDetailSerializer, PostSerializer, \
    UserSerializer


class CreatePost(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        # Default creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Feed(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PostDetailSerializer
    pagination_class = None

    def get_serializer_context(self):
        context = super(Feed, self).get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        posts_qs = Post.objects.all()
        if self.request.query_params.get('profile'):
            posts_qs = posts_qs.filter(creator=User.objects.get(id=self.request.query_params['user']))
        elif self.request.query_params.get('snip'):
            posts_qs = posts_qs.filter(users_who_snipped=User.objects.get(id=self.request.query_params['user']))
        return posts_qs


class Languages(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = LanguageDetailSerializer
    pagination_class = None
    queryset = Language.objects.all()


class CreateComment(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CommentSerializer


class ClickLike(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request) -> Response:
        post = Post.objects.get(id=request.data['post'])
        user = User.objects.get(id=request.data['user'])
        if user not in post.users_who_likes.all():
            post.users_who_likes.add(user)
        else:
            post.users_who_likes.remove(user)
        post.save()

        return Response(PostDetailSerializer(instance=post, context={'request': self.request}).data,
                        status=status.HTTP_202_ACCEPTED)


class ClickSnip(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request) -> Response:
        post = Post.objects.get(id=request.data['post'])
        user = User.objects.get(id=request.data['user'])
        if user not in post.users_who_snipped.all():
            post.users_who_snipped.add(user)
        else:
            post.users_who_snipped.remove(user)
        post.save()

        return Response(PostDetailSerializer(instance=post, context={'request': self.request}).data,
                        status=status.HTTP_202_ACCEPTED)


class CreateUser(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Default creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # Log user
        user = User.objects.get(username=request.data['username'], password=request.data['password'])
        user.logged = True
        user.save()
        User.objects.exclude(username=user.username).update(logged=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GetUser(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Login(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request: Request) -> Response:
        user = User.objects.filter(username=request.data['username'], password=request.data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user = user.first()
        user.logged = True
        user.save()
        User.objects.exclude(username=user.username).update(logged=False)
        return Response(status=status.HTTP_200_OK)


class LoggedUser(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request: Request) -> Response:
        user_qs = User.objects.filter(logged=True)
        if not user_qs:
            user = User.objects.first()
            user.logged = True
            user.save()
        else:
            user = user_qs.first()
        User.objects.exclude(username=user.username).update(logged=False)
        return Response(UserSerializer(instance=user).data, status=status.HTTP_200_OK)
