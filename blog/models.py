from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Subject(models.Model):
    BRANCH_CHOICES=(
        ("CIVIL","Civil Engineering"),
        ("MECH","Mechanical Engineering"),
        ("ECE", "Electronics & Communication Engineering"),
        ("CSE", "Computer Science Engineering")
    )
    subject_name = models.CharField(max_length=300, help_text="Add the subject you want to create articles about.")
    subject_description = RichTextField(config_name='awesome_ckeditor')
    branch = models.CharField(choices=BRANCH_CHOICES, default="CIVIL", max_length=100)

    # def get_absolute_url(self):
    #     return reverse('blog:subject_articles_list', kwargs={'pk': self.pk})

    def published_articles(self):
        return self.articles.filter(published_date__lte=timezone.now()).order_by('published_date')

    def __str__(self):
        return self.subject_name

class Chapter(models.Model):
    subject_name = models.ForeignKey(Subject, related_name='chapters', on_delete=models.CASCADE)
    chapter_name = models.CharField(max_length=300)
    chapter_number = models.IntegerField(default=0)

    class Meta:
        ordering = ['chapter_number']


    def get_absolute_url(self):
        return reverse('blog:subject_content', kwargs={'pk': self.subject_name.pk})

    def __str__(self):
        return self.chapter_name

class Article(models.Model):
    subject_name = models.ForeignKey(Subject, related_name='articles', on_delete=models.CASCADE)
    chapter_name = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    article_number = models.IntegerField(default=0)
    # article_content = models.TextField()
    article_content = RichTextField(config_name='awesome_ckeditor')
    # references = models.TextField(blank=True, null=True)
    references = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['chapter_name','article_number']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author_email = models.EmailField(max_length=200, blank=False, default='user@Engineers.com')
    author = models.TextField(blank=False, max_length=300)
    comment_content = models.TextField(blank=False)
    created_date = models.DateTimeField(default = timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.author + "; "+self.comment_content
