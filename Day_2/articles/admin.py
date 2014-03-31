from django.contrib import admin
#import the models to register in the admin
from .models import Article

#admin class to refine admin interface
class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	fields = ('author','title','content','slug')
	list_display = ['title','author','created_at']
	list_display_links = ['title']
	
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ['title','author','created_at']

#Register the models so the admin interface can 
# see and manage the Models
admin.site.register(Article,PostAdmin)

