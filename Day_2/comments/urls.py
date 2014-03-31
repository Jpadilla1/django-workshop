from django.conf.urls import patterns, include, url
from .views import CommentListView

#url patterns representated by regular expresion strings
urlpatterns = patterns(
    '',

    url(r'^(?P<slug>[\w-]+)/$',CommentListView.as_view(), name = 'comment_list'),
 
)