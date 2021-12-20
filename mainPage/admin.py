from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from .models import User


UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active', 'is_staff', 'is_superuser', 'groups', 'phone', 'address', 'about',
    'user_permissions', 'membership', 'birth_date', 'img_avatar', 'img_avatar_upload'
)

admin.site.register(User, UserAdmin)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.PostDescription)
class PostDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PostImgUrl)
class PostImgAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_url']
    list_editable = ['img_url']


@admin.register(models.SmartPhone)
class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'img_primary', 'brand']
    list_editable = ['brand', 'img_primary']
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
