# Generated by Django 3.2.9 on 2021-12-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_auto_20211209_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
