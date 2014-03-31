from django.conf.urls import patterns, include, url
from .views import ArticleListView, ArticleDetailView

#url patterns representated by regular expresion strings

urlpatterns = patterns(
    '',
    url(r'^$',ArticleListView.as_view(), name = 'article_list'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetailView.as_view(), name = 'article_detail'),
)