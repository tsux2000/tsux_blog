from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.IntegerField(unique = True,)
    status_id = models.IntegerField()
    position_id = models.IntegerField(blank = True,)
    slug = models.SlugField(unique = True,)
    first_name = models.CharField(max_length = 255,)
    last_name = models.CharField(max_length = 255, blank = True,)
    disp_name = models.CharField(max_length = 255, unique = True,)
    password = models.CharField(max_length = 255,)
    birth_date = models.DateField(blank = True,)
    phone = models.SlugField(blank = True,)
    email = models.EmailField()
    bio = models.TextField(blank = True,)
    create_date = models.DateField(default = timezone.now,)
    update_date = models.DateField(auto_now = True,)
    user_img = models.SlugField(blank = True,)

    # class Meta:
    #     abstract = True

class AdminUser(User):
    admin_user_id = User.user_id

class CommonUser(User):
    common_user_id = User.user_id

class Post(models.Model):
    post_id = models.IntegerField(unique = True,)
    slug = models.SlugField(unique = True,)
    category_id = models.IntegerField()
    subcategory_id = models.IntegerField(blank = True,)
    author_id = models.IntegerField()
    status_id = models.IntegerField()
    title = models.CharField(max_length = 255, unique = True,)
    description = models.TextField(blank = True,)
    keywords = models.CharField(max_length = 255, blank = True,)
    contents = models.TextField(unique = True,)
    thumbnail = models.SlugField(blank = True,)
    create_date = models.DateField(default = timezone.now)
    update_date = models.DateField(auto_now = True,)

class Comment(models.Model):
    comment_id = models.IntegerField(unique = True,)
    title = models.CharField(max_length = 255, blank = True,)
    user_id = models.IntegerField()
    contents = models.TextField()
    post_id = models.IntegerField(blank = True,)
    status_id = models.IntegerField()
    create_date = models.DateField(default = timezone.now)

class Attr(models.Model):
    attr_id = models.IntegerField(unique = True,)
    slug = models.SlugField(unique = True,)
    name = models.CharField(max_length = 255, unique = True,)
    status_id = models.IntegerField()

    class Meta:
        abstract = True

class Category(Attr):
    category_id = Attr.attr_id

class SubCategory(Attr):
    sub_category_id = Attr.attr_id

class Status(Attr):
    status_id = Attr.attr_id

class Tag(Attr):
    tag_id = Attr.attr_id

class Position(Attr):
    position_id = Attr.attr_id
