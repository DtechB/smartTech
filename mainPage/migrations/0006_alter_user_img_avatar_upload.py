# Generated by Django 3.2.9 on 2021-12-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0005_alter_user_img_avatar_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_avatar_upload',
            field=models.ImageField(blank=True, default='images/img.png', null=True, upload_to='images'),
        ),
    ]
