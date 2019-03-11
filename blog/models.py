from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=120, help_text='Title for '
                                                                             'the post')
    content = models.TextField(verbose_name='content', max_length=500, help_text='The content for the post')
    date_posted = models.DateTimeField(default=timezone.now)
    # if the user is deleted then all the posts of the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})

