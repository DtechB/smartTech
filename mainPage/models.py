from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class User(AbstractUser):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    img_avatar = models.CharField(max_length=2083,
                                  default='https://png.pngtree.com/png-vector/20190710/ourmid/pngtree-user-vector'
                                          '-avatar-png-image_1541962.jpg')
    img_avatar_upload = models.ImageField(upload_to="images", null=True, blank=True, default="images/img.png")
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    def get_img_upload(self):
        return format_html("<img src='{}'>".format(self.img_avatar_upload.url))


class Post(models.Model):
    STATUS_DRAFT = 'D'
    STATUS_PUBLISHED = 'P'
    STATUS = [
        ('D', 'draft'),
        ('P', 'published')
    ]
    post_id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS_DRAFT)
    publish = models.DateTimeField(auto_now=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment_user = models.ManyToManyField(User, through='Comment')
    img_primary = models.CharField(max_length=2083, null=True)
    userpost = models.ManyToManyField(User, related_name='user', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post', args=[self.slug, self.post_id])


class PostDescription(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostImgUrl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    img_url = models.CharField(max_length=2083)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class SmartPhone(models.Model):
    smartphone_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    time_release = models.DateField(null=True)
    slug = models.SlugField(default='+')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    user = models.ManyToManyField(User, null=True, blank=True)
    img_primary = models.CharField(max_length=2083, null=True)

    def get_absolute_url(self):
        return reverse('phone:single_phone', args=[self.slug, self.smartphone_id])


class SmartPhoneDescription(models.Model):
    id = models.BigIntegerField(primary_key=True)
    description = models.TextField()
    smartphone = models.ForeignKey(SmartPhone, on_delete=models.CASCADE)


class SmartPhoneImgUrl(models.Model):
    id = models.BigIntegerField(primary_key=True)
    img_url = models.CharField(max_length=2083)
    smartphone = models.ForeignKey(SmartPhone, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True)
    body = models.TextField()
