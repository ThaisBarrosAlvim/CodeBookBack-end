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
        fields = ('icon', 'name', 'id')


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'creator')

    creator = UserDetailSerializer(many=False, read_only=True)


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image', 'creator', 'language', 'comments', 'liked','snipped')

    creator = UserDetailSerializer(many=False, read_only=True)
    language = LanguageDetailSerializer(many=False, read_only=True)
    comments = CommentDetailSerializer(many=True, read_only=True)
    liked = serializers.SerializerMethodField()
    snipped = serializers.SerializerMethodField()

    def get_liked(self, obj: Post):
        if self.context['request'].query_params:
            user_id = self.context['request'].query_params['user']
        else:
            user_id = self.context['request'].data['user']
        return bool(obj.users_who_likes.filter(id=user_id))

    def get_snipped(self, obj: Post):
        if self.context['request'].query_params:
            user_id = self.context['request'].query_params['user']
        else:
            user_id = self.context['request'].data['user']
        return bool(obj.users_who_snipped.filter(id=user_id))


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
