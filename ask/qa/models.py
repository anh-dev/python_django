from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
  title = models.CharField()
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  rating = models.IntegerField()
  author = models.ForeignKey(User, on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User,related_name='question_like_user')

class Answer(models.Model):
  
  text = models.TextField()
  added_at = models.DateField(auto_now_add=True)
  question = models.OneToOneField(Question)
  author = models.ForeignKey(User, on_delete=models.SET_NULL)
  def new(self):
     return self.order_by('-added_at')
  def popular(self):
     return self.order_by('-rating')
        
