from django.contrib import admin
from django.utils.safestring import mark_safe
from dojo.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tags', 'content_size', 'lnglat']
    list_editable = ['title']
    # list_display_links = ['id', 'title']
    list_filter = ['tags']

    def content_size(self, post):
        html = '<span style="color: blue;">{}</span>글자'.format(len(post.content))
        return mark_safe(html)

    content_size.short_decription = '내용 글자수'
    # content_size.allow_tags = True
