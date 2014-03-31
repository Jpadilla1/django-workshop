from django.views.generic import DetailView,ListView

from .models import Article
#class representation of a View
class ArticleListView(ListView):
	template_name = "article_list.html"
	model = Article


class ArticleDetailView(DetailView, ):
	template_name = 'article_detail.html'
	model = Article

