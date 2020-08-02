from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import (Article, Subject, Comment, Chapter)
from blog.forms import (ArticleForm, SubjectForm, CommentForm, ChapterForm)
from django.views import View
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)

# Create your views here.
#About View
class AboutView(TemplateView):
    template_name = "about.html"

class SubjectListView(ListView):
    model = Subject

class CreateSubjectView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/subject_form.html'
    form_class = SubjectForm
    model = Subject

class CreateChapterView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    template_name = 'chapter_form.html'
    redirect_field_name = 'blog/article_list.html'
    form_class = ChapterForm
    model = Chapter


class CreateArticleView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/article_form.html'
    form_class = ArticleForm
    model = Article

class UpdateArticleView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm
    model = Article

class DeleteArticleView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Article
    success_url = reverse_lazy('blog:subject_list')

class ArticleDetailView(DetailView):
    model=Article

def subject_content(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    chapters = Chapter.objects.filter(subject_name__pk=pk)
    articles = Article.objects.filter(subject_name__pk=pk).filter(published_date__isnull=False)
    context = {
        'subject':subject,
        'chapters':chapters,
        'articles':articles,
    }
    return render(request, 'subject_content.html', context=context)

class DraftsArticleListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Article
    success_url = reverse_lazy('blog:article_drafts')

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).filter(author__username=self.request.user.username).order_by('created_date')


@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('blog:article_detail', pk=pk)
