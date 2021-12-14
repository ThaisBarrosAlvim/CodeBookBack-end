from rest_framework import serializers

from codebook.models import Comment, Language, Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'creator', 'language')

    language = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True,
                                                  queryset=Language.objects.all())
    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True,
                                                 queryset=User.objects.all())


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_image', 'username')


class LanguageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('icon', 'name')


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'creator')

    creator = UserDetailSerializer(many=False, read_only=True)


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('image', 'creator', 'language', 'comments')

    creator = UserDetailSerializer(many=False, read_only=True)
    language = LanguageDetailSerializer(many=False, read_only=True)
    comments = CommentDetailSerializer(many=True, read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'creator', 'post')

    creator = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True,
                                                 queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(many=False, read_only=False, required=True,
                                              queryset=Post.objects.all())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile_image', 'email')
