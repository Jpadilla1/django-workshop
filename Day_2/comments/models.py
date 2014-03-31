from django.db import models

from articles.models import Article


# Class representation of a database table
class Comment(models.Model):
    article = models.ForeignKey(Article)
    content = models.TextField()
    created_by = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.content
