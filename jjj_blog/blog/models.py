from email.policy import default
from django.db import models
from django.forms import BooleanField
from markdownx.models import MarkdownxField
from datetime import timedelta



class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100)
    key = models.CharField(max_length=20)
    tags = models.ManyToManyField(Tag)
    content = MarkdownxField()
    is_public = models.BooleanField('ON: private, OFF: public', default=False)
    pub_date = models.DateTimeField('DATE')
    
    
    class Meta:
        ordering = ['-pub_date']
    
    
    def __str__(self):
        JST_date = self.pub_date + timedelta(hours=9)
        return f'{JST_date.date()}_{self.key}' # create & update date(JST) + key 
