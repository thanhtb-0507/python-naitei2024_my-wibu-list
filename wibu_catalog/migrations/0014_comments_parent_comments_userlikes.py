# Generated by Django 5.1 on 2024-08-28 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibu_catalog', '0013_merge_20240827_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='wibu_catalog.comments'),
        ),
        migrations.AddField(
            model_name='comments',
            name='userLikes',
            field=models.ManyToManyField(blank=True, help_text='Users who liked the comment.', related_name='liked_comments', to='wibu_catalog.users'),
        ),
    ]
