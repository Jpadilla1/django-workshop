from django.db import models


# Class representation of a database table
class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.count()
