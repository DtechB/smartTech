# Generated by Django 3.2.9 on 2021-12-08 13:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='-')),
                ('category', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('D', 'draft'), ('P', 'published')], default='D', max_length=1)),
                ('publish', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('membership', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'Gold')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhoneImgUrl',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('img_url', models.CharField(max_length=255)),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.post')),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhoneDescription',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('smartphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.post')),
            ],
        ),
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('smartphone_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('memory', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('body', models.CharField(max_length=255)),
                ('network', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('battery', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('time_release', models.DateField(null=True)),
                ('slug', models.SlugField(default='+')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainPage.user')),
            ],
        ),
        migrations.CreateModel(
            name='PostImgUrl',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('img_url', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostDescription',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comment_user',
            field=models.ManyToManyField(through='mainPage.Comment', to='mainPage.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to='mainPage.user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.user'),
        ),
    ]
