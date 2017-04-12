import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):

    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdraw')
    ]

    TAG_CHOICES = [
        ('science', '과학'),
        ('economy', '경제'),
        ('politics', '정치'),
        ('sports', '스포츠')
    ]

    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    status = models.CharField(max_length=1,
                            choices=STATUS_CHOICES, default='d')
    tags = models.CharField(max_length=100,
                            blank=True,
                            choices=TAG_CHOICES,
                            default='science')
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              blank=True,
                              help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    test_field = models.IntegerField(default=10)

    reporter = models.ForeignKey('Reporter', null=True, verbose_name='기자')

    # def get_reporter(self):
    #     try:
    #         return self.reporter.name
    #     except:
    #         return 'unknown'
    # get_reporter.short_description = '기자'


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
