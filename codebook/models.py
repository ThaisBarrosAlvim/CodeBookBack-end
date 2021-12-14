from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.CharField(verbose_name='Language', max_length=21)
    icon = models.ImageField(verbose_name='Icon', upload_to='languages_icons')


class User(models.Model):
    username = models.CharField(verbose_name='Username', max_length=255)
    password = models.CharField(verbose_name='Password', max_length=255)
    profile_image = models.ImageField(verbose_name='Profile Image', null=True, upload_to='profile_images')
    email = models.EmailField(verbose_name='E-mail')

    liked_posts = models.ManyToManyField('Post', related_name='users_who_likes')
    snipped_posts = models.ManyToManyField('Post', related_name='users_who_snipped')


class Comment(models.Model):
    text = models.TextField(verbose_name='Text')
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')


class Post(models.Model):
    likes = models.IntegerField(verbose_name='Likes', default=0)
    image = models.ImageField(verbose_name='Image')
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    create_date = models.DateTimeField(verbose_name='Create Date', auto_now=True)
    language = models.ForeignKey('Language', on_delete=models.DO_NOTHING, null=True)
