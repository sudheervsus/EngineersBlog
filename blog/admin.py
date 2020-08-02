from django.contrib import admin
from blog.models import Subject, Article, Comment, Chapter

# Register your models here.
admin.site.register(Subject)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Chapter)
