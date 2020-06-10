from django import forms
from blog.models import ( Topic, Article )
from ckeditor.widgets import CKEditorWidget

class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = ['topic_name']
        labels = {
            'topic_name':'Subject/Topic'
        }
        widgets = {
            'topic_name': forms.TextInput(attrs = {'class': 'form-control'})
        }

class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        fields = [ 'topic_name', 'author', 'title', 'article_content', 'references']
        labels ={
            'topic_name':'Subject/Topic',
            'article_content': 'Article',
        }
        widgets = {
            'topic_name':forms.Select(attrs = {'class':'form-control'}),
            'author':forms.Select(attrs = {'class':'form-control'}),
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            # 'article_content': forms.Textarea(attrs = {'class':'form-control'}),
            'article_content': CKEditorWidget(config_name='awesome_ckeditor'),
            'references':CKEditorWidget(config_name='awesome_ckeditor'),
            # 'references':forms.Textarea(attrs = {'class':'form-control'}),
        }
