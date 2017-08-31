from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	objects = QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User, default="None")
	likes = models.ManyToManyField(User, related_name="question-like-user+")
	def __str__(self):
		return self.title
'''
class Likes(models.Model):
	question = models.ForeignKey(Question, related_name="like_question")
	user = models.ForeignKey(User, related_name="like_user")
'''

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question, null = True)
	author = models.ForeignKey(User, default = "None")
	def __str__(self):
		return self.text
