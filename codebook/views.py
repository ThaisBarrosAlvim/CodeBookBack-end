# Create your views here.
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from codebook.models import Language, Post
from codebook.serializers import CommentSerializer, LanguageDetailSerializer, PostDetailSerializer, PostSerializer, \
    UserSerializer


class CreatePost(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PostSerializer


class Feed(ListAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = PostDetailSerializer
    pagination_class = None
    queryset = Post.objects.all()


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


class CreateUser(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
