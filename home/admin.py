from django.contrib import admin
from .models import BlogPost, Contact, Category, Comment

admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Comment)
