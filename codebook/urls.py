from django.urls import path

from codebook.views import ClickLike, ClickSnip, CreateComment, CreatePost, CreateUser, Feed, GetUser, Languages, \
    LoggedUser, Login

app_name = "codebook"

urlpatterns = [
    path('api/create_post', CreatePost.as_view(), name='create_post'),
    path('api/create_user', CreateUser.as_view(), name='create_user'),
    path('api/user/<int:pk>', GetUser.as_view(), name='get_user'),
    path('api/login', Login.as_view(), name='login'),
    path('api/get_logged', LoggedUser.as_view(), name='get_logged'),
    path('api/create_comment', CreateComment.as_view(), name='create_comment'),
    path('api/feed', Feed.as_view(), name='feed'),
    path('api/languages', Languages.as_view(), name='languages'),
    path('api/click_like', ClickLike.as_view(), name='click_like'),
    path('api/click_snip', ClickSnip.as_view(), name='click_snip'),
]
