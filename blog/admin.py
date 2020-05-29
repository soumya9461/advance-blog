from django.contrib import admin
from .models import *

# class PostAdmin(admin.ModelAdmin):
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'created_date', 'published_date')
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    filter_horizontal = ('category',)
    

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Category)
