# Generated by Django 3.2.12 on 2022-03-18 04:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('post_content', models.CharField(max_length=2000)),
                ('post_comment_count', models.IntegerField(default=0)),
                ('post_title', models.CharField(max_length=200)),
                ('post_isdeleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment_modified', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment_content', models.CharField(max_length=200)),
                ('comment_isdeleted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
