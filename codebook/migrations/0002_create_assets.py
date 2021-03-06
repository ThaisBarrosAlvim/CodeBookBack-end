# Generated by Django 4.0 on 2021-12-14 00:16
from typing import TYPE_CHECKING

from django.db import migrations

if TYPE_CHECKING:
    from codebook.models import Language,User


def create_languages(apps, schema_editor):
    # Create default languages
    language_model: 'Language' = apps.get_model('codebook', 'Language')
    languages = [
        language_model(name='Python', icon='languages_icons/python.png'),
        language_model(name='JavaScript', icon='languages_icons/js-logo.png'),
        language_model(name='Ruby', icon='languages_icons/ruby-logo.png'),
        language_model(name='HTML', icon='languages_icons/html-logo.png'),
        language_model(name='CSS', icon='languages_icons/css-logo.png'),
    ]
    language_model.objects.bulk_create(languages)

    # Create default User
    user_model: 'User' = apps.get_model('codebook', 'User')
    user = user_model(username='TestUser', email='test@test.com', password='123')
    user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('codebook', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_languages)
    ]
