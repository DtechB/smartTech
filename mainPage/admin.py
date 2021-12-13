from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug']
    prepopulated_fields = {
        'slug': ['title']
    }
    exclude = ('user',)


@admin.register(models.PostDescription)
class PostDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostImgUrl)
class PostImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_url']
    list_editable = ['img_url']


@admin.register(models.SmartPhone)
class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'brand']
    list_editable = ['brand']
    prepopulated_fields = {
        'slug': ['name']
    }
    exclude = ('user',)


@admin.register(models.SmartPhoneDescription)
class SmartPhoneDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SmartPhoneImgUrl)
class SmartPhoneImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_url']
    list_editable = ['img_url']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['date_time']
