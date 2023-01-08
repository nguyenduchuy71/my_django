from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_content', 'post_title', 'post_comment_count',
                    'post_created', 'post_modified', 'post_isdeleted')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_content', 'post', 'author',
                    'comment_isdeleted', 'comment_created', 'comment_modified')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
