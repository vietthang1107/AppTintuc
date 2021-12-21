from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.


class New(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    author = models.TextField(blank=True, null=True, default='')

    class Meta:
        ordering = ['date_created']


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    new = models.ForeignKey(
        New, verbose_name=('Id of new'), on_delete=CASCADE)
    date_created = models.DateTimeField(default=timezone.now, editable=False)
    content = models.TextField(blank=True, null=True, default='')
    user_comment = models.TextField(blank=True, null=True, default='')
