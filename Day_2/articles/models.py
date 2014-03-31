from django.db import models


# Class representation of a database table
class Article(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20, unique = True)#added unique = True Field to prevent Duplicate titles
    #added slug field for readable urls 
    slug = models.SlugField(max_length = 255, blank = True, default = '')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def comment_count(self):
        return self.comment_set.count()
