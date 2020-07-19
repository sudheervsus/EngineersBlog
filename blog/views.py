from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import (Article, Topic, Comments)
from blog.forms import (ArticleForm, TopicForm)
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,)

# Create your views here.
#About View
class AboutView(TemplateView):
    template_name = "about.html"

class TopicListView(ListView):
    model = Topic

class TopicArticlesListView(ListView):
    template_name = 'article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(topic_name__pk = self.kwargs['pk']).filter(published_date__isnull=False)

class CreateTopicView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'blog/topic_form.html'
    form_class = TopicForm
    model = Topic

# def TopicArticlesListView(request, pk):
#     article_list = Article.objects.filter(topic_name__pk = pk).filter(published_date__isnull=False)
#     print(article_list)
#     return render(request,'article_list.html',{'article_list':article_list})

class AuthorArticlesListView(ListView):
    template_name = 'article_list.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.filter(author__pk = self.kwargs['pk']).filter(published_date__isnull=False).order_by('-created_date')

# #Needs To be worked on. *****INCOMPLETE*****
# def AuthorArticlesListView(request, pk):
#     article_list = Article.objects.filter(author__pk = pk).filter(published_date__isnull=False).order_by('-created_date')
#     return render(request,'article_list.html',{'article_list':article_list})


class ArticleDetailView(DetailView):
    model = Article

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        comments = Comments.objects.filter(title__pk = pk).order_by('-created_date')
        return render(request, 'article_detail.html', {'article':article, 'comments':comments})

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.title = article
            comment.save()
            return redirect('blog:article_detail', pk=pk)

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
    success_url = reverse_lazy('blog:topic_list')

class DraftsArticleListView(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('blog:article_detail', pk=pk)
