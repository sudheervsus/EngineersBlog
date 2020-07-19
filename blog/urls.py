from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),
    path('topics/<int:pk>/', views.TopicArticlesListView.as_view(), name ='topic_articles_list'),
    path('topics/createnew/', views.CreateTopicView.as_view(), name='topic_create_new'),
    path('author/<int:pk>/', views.AuthorArticlesListView.as_view(), name ='author_articles_list'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/createnew/', views.CreateArticleView.as_view(), name='article_create_new'),
    path('article/<int:pk>/edit/', views.UpdateArticleView.as_view(), name='article_edit'),
    path('article/<int:pk>/publish/', views.article_publish, name='article_publish'),
    path('article/<int:pk>/remove/', views.DeleteArticleView.as_view(), name='article_remove'),
    path('drafts/', views.DraftsArticleListView.as_view(), name='article_drafts'),
    path('about/', views.AboutView.as_view(), name='about'),

]
