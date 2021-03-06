# Generated by Django 3.1.13 on 2022-02-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_title', models.CharField(max_length=30)),
                ('info_content', models.TextField()),
                ('info_published', models.DateTimeField()),
                ('info_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=30)),
                ('video_content', models.TextField()),
                ('video_author', models.CharField(max_length=50)),
                ('video_published', models.DateTimeField()),
            ],
        ),
    ]
