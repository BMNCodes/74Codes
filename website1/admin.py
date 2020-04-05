from django.contrib import admin
from .models import News, Comment

class NewsAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'status', 'created')
    list_filter = ('title', 'author', 'status', 'created')
    search_fields= ('title', 'body')


class CommentAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'news', 'created')
    list_filter = ('created', 'active')
    search_fields= ('name', 'email')

admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
