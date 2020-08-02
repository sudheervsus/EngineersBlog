from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', views.subject_content, name='subject_content'),
    path('subjects/createnew/', views.CreateSubjectView.as_view(), name='subject_create_new'),
    path('chapters/createnew/', views.CreateChapterView.as_view(), name='chapter_create_new'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/createnew/', views.CreateArticleView.as_view(), name='article_create_new'),
    path('article/<int:pk>/edit/', views.UpdateArticleView.as_view(), name='article_edit'),
    path('article/<int:pk>/publish/', views.article_publish, name='article_publish'),
    path('article/<int:pk>/remove/', views.DeleteArticleView.as_view(), name='article_remove'),
    path('drafts/', views.DraftsArticleListView.as_view(), name='article_drafts'),
    path('about/', views.AboutView.as_view(), name='about'),

]
