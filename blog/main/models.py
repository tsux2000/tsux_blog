from django.db import models

class User(models.Model):
    user_id = models.Field()
    status_id = models.Field()
    position_id = models.Field()
    slug = models.Field()
    first_name = models.Field()
    middle_name = models.Field()
    last_name = models.Field()
    disp_name = models.Field()
    password = models.Field()
    birth_date = models.Field()
    phone = models.Field()
    bio = models.Field()
    create_date = models.Field()
    update_date = models.Field()
    user_img_id = models.Field()

    def __str__(self):
        return self.id + "_" + self_slug

class AdminUser(User):
    admin_user_id = user_id

class CommonUser(User):
    common_user_id = user_id

class Post(models.Model):
    post_id = models.Field()
    slug = models.Field()
    category_id = models.Field()
    subcategory_id = models.Field()
    author_id = models.Field()
    status_id = models.Field()
    tag_id = models.Field()
    title = models.Field()
    description = models.Field()
    keywords = models.Field()
    contents = models.Field()
    thumbnail = models.Field()
    create_date = models.Field()
    update_date = models.Field()

class Comment(models.Model):
    comment_id = models.Field()
    title = models.Field()
    user_id = models.Field()
    content = models.Field()
    post_id = models.Field()
    status_id = models.Field()
    create_date = models.Field()

class Attr(models.Model):
    attr_id = models.Field()
    slug = models.Field()
    name = models.Field()
    status_id = models.Field()

class Category(Attr):
    category_id = attr_id

class SubCategory(Attr):
    sub_category_id = attr_id

class Status(Attr):
    status_id = attr_id

class Position(Attr):
    position_id = attr_id
