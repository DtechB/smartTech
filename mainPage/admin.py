from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'status']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.PostDescription)
class PostDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostImgUrl)
class PostImgAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SmartPhone)
class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'score']
    prepopulated_fields = {
        'slug': ['name']
    }


@admin.register(models.SmartPhoneDescription)
class SmartPhoneDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SmartPhoneImgUrl)
class SmartPhoneImgAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['date_time']
