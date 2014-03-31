from django.views.generic import ListView
from .models import Comment

#class representation of a View in Django
class CommentListView(ListView):
	template_name = 'comment_list.html'
	model = Comment
