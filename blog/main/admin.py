from django.contrib import admin
from .models import Comment, Post, AdminUser, Category, CommonUser, Position, Status, SubCategory

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(AdminUser)
admin.site.register(Category)
admin.site.register(CommonUser)
admin.site.register(Position)
admin.site.register(Status)
admin.site.register(SubCategory)
