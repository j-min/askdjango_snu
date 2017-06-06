import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Thumbnail

from .validators import lnglat_validator, min_length_3_validator

class Post(models.Model):

    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw')
    ]

    # TAG_CHOICES = [
    #     ('science', '과학'),
    #     ('economy', '경제'),
    #     ('politics', '정치'),
    #     ('sports', '스포츠')
    # ]

    title = models.CharField(max_length=100, verbose_name='제목', validators=[min_length_3_validator])
    content = models.TextField(help_text='Markdown 문법을 써주세요.')

    # photo = models.ImageField(blank=True, upload_to='dojo/post/%Y/%m/%d')
    # photo_thumbnail = ImageSpecField(source='photo',
    #     processors=[Thumbnail(300, 300)],
    #     format='JPEG',
    #     options={'quality': 60}
    # )

    photo = ProcessedImageField(blank=True, upload_to='dojo/post/%Y/%m/%d',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60}
    )


    status = models.CharField(max_length=1,
                            choices=STATUS_CHOICES, default='d')
    tag_set = models.ManyToManyField('Tag')
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              blank=True,
                              help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)

    # ordering
    class Meta:
        ordering = ['-id']

    reporter = models.ForeignKey('Reporter', null=True, verbose_name='기자')

    def get_tags(self):
        try:
            return ", ".join([tag.name for tag in self.tag_set.all()])
        except:
            return 'no tags'
    get_tags.short_description = 'Tags'

    def __str__(self):
        return self.title

class Reporter(models.Model):
    name = models.CharField(max_length=20, default='unknown 기자', verbose_name='이름')
    def __str__(self):
        return self.name

    def get_posts(self):
        # posts = []
        try:
            return str(Post.objects.filter(reporter=self)[0])
        except:
            return 'no post'
    get_posts.short_description = '첫 기사'


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
