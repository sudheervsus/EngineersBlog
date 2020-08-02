from django import forms
from blog.models import ( Subject, Article, Chapter, Comment )
from ckeditor.widgets import CKEditorWidget

class SubjectForm(forms.ModelForm):
    class Meta():
        model = Subject
        fields = ['subject_name', 'branch', 'subject_description']
        labels = {
            'subject_name':'Subject',
            'subject_description':'Description'
        }
        widgets = {
            'subject_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'branch': forms.Select(attrs = {'class': 'form-control'}),
            'subject_description': CKEditorWidget(config_name='awesome_ckeditor'),
        }

class ChapterForm(forms.ModelForm):
    class Meta():
        model = Chapter
        fields = ['subject_name', 'chapter_name', 'chapter_number']

        widgets = {
            'subject_name':forms.Select(attrs = {'class':'form-control'}),
            'chapter_name':forms.TextInput(attrs = {'class':'form-control'}),
            'chapter_number':forms.NumberInput(attrs = {'class':'form-control'}),
        }


class ArticleForm(forms.ModelForm):

    class Meta():
        model = Article
        fields = [ 'subject_name', 'chapter_name', 'author', 'title', 'article_number', 'article_content', 'references']
        labels ={
            'subject_name':'Subject',
            'article_content': 'Article',
        }
        widgets = {
            'subject_name':forms.Select(attrs = {'class':'form-control'}),
            'chapter_name':forms.Select(attrs = {'class':'form-control'}),
            'author':forms.Select(attrs = {'class':'form-control'}),
            'title':forms.TextInput(attrs = {'class':'form-control'}),
            'article_number': forms.NumberInput(attrs = {'class':'form-control'}),
            # 'article_content': forms.Textarea(attrs = {'class':'form-control'}),
            'article_content': CKEditorWidget(config_name='awesome_ckeditor'),
            'references':CKEditorWidget(config_name='awesome_ckeditor'),
            # 'references':forms.Textarea(attrs = {'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ['author', 'author_email', 'comment_content']
        labels ={
            'author':'Name',
            'author_email':'Email',
            'comment_content': 'Comment',
        }

    widgets = {
        'author':forms.TextInput(attrs = {'class':'form-control'}),
        'author_email':forms.EmailInput(attrs = {'class':'form-control'}),
        'comment_content': forms.Textarea(attrs = {'class':'form-control'}),
    }
