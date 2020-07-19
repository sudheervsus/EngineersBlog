from django.contrib import admin
from blog.models import Topic, Article, Comments

# Register your models here.
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Comments)
