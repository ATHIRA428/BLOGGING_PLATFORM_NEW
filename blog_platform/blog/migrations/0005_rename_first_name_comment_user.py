# Generated by Django 4.2.3 on 2023-07-25 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_user_comment_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='first_name',
            new_name='user',
        ),
    ]
