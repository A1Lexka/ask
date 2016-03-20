from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=20)
    likes = models.ForeignKey(User)
    def __str__(self):              
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=100)
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.text
