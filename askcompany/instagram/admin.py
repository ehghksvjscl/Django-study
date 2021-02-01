from django.contrib import admin
from .models import Post, Comment, Tag

from django.utils.safestring import mark_safe

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag','message','message_count','is_public','created_at','updated_at']
    list_display_links = ['message']
    list_filter = ['is_public','created_at']
    search_fields = ['message']

    # Admin Page에 Img보여주기
    def photo_tag(self,post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;"/>')
        return None

    def message_count(self,post):
        return f"{len(post.message)} 글자"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass