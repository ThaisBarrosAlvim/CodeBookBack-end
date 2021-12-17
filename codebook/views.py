# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView
from codebook.models import Language, Post, User
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

    def get(self, request) -> Response:


        return Response()


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
        post = Post.objects.get(id=request['post_id'])
        user = User.objects.get(id=request['user_id'])
        if user not in post.users_who_likes.all():
            post.likes += 1
            post.users_who_likes.add(user)
            # user.liked_posts.add(post)
        else:
            post.likes += 1
            post.users_who_likes.remove(user)
            # user.liked_posts.remove(post)
        post.save()
        # user.save()

        return Response(PostSerializer(instance=post).data, status=status.HTTP_202_ACCEPTED)


class CreateUser(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer


class GetUser(RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer
    queryset = User.objects.all()
