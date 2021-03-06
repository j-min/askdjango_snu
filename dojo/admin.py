from django.contrib import admin
from django.utils.safestring import mark_safe
from dojo.models import Post, Reporter, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'reporter', 'get_tags', 'content_size', 'status', 'created_at', 'updated_at']
    list_editable = ['title', 'reporter']
    search_field = ['title', 'reporter']
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

    # def get_tags(self, post):
    #     return "\n".join([tag.name for tag in post.tag_set.all()])


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_posts']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
