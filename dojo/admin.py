from django.contrib import admin
from django.utils.safestring import mark_safe
from dojo.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tags', 'content_size', 'status']
    list_editable = ['title', 'tags']
    search_field = ['title']
    # list_display_links = ['id', 'title']
    list_filter = ['created_at', 'status']
    actions = ['make_published']

    def make_published(self, request, queryset):
        total = queryset.update(status='p')
        self.message_user(request, '{}건을 발행했습니다.'.format(total))
    make_published.short_decription = '선택된 항목을 발행하기'

    def content_size(self, post):
        html = '<span style="color: blue;">{}</span>글자'.format(len(post.content))
        return mark_safe(html)

    content_size.short_decription = '내용 글자수'
    # content_size.allow_tags = True
