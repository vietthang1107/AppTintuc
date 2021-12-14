from django.db import models

# Create your models here.


class New(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    author = models.TextField()

    class Meta:
        ordering = ['created']
