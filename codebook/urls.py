from django.urls import path

from codebook.views import CreateComment, CreatePost, CreateUser, Feed, GetUser, Languages

app_name = "codebook"

urlpatterns = [
    path('api/create_post', CreatePost.as_view(), name='create_post'),
    path('api/create_user', CreateUser.as_view(), name='create_user'),
    path('api/user/<int:pk>', GetUser.as_view(), name='get_user'),
    path('api/create_comment', CreateComment.as_view(), name='create_comment'),
    path('api/feed', Feed.as_view(), name='feed'),
    path('api/languages', Languages.as_view(), name='languages'),
]
