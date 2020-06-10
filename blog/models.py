from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=300, help_text="Add the subject/topic you want to create articles about.")

    def get_absolute_url(self):
        return reverse('blog:topics_list', kwargs={'pk': self.pk})

    def published_articles(self):
        return self.articles.filter(published_date__lte=timezone.now()).order_by('published_date')

    def __str__(self):
        return self.topic_name

class Article(models.Model):
    topic_name = models.ForeignKey(Topic, related_name='articles', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    # article_content = models.TextField()
    article_content = RichTextField(config_name='awesome_ckeditor')
    # references = models.TextField(blank=True, null=True)
    references = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
