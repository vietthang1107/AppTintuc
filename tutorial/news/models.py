from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.


class New(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, null=True, default='')
    author = models.TextField(blank=True, null=True, default='')

    class Meta:
        ordering = ['created']
