from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('blog:topics_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.topic_name

class Article(models.Model):
    topic_name = models.ForeignKey(Topic, related_name='articles', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    article_content = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
