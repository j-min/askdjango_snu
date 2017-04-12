import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

choices = ['과학', '경제', '정치']
choices = ((i, choice) for i, choice in enumerate(choices))


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    tags = models.CharField(max_length=100,
                            blank=True,
                            choices=choices)
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              help_text='경도, 위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)
