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
	rating = models.IntegerField()
	author = models.ForeignKey(User)
	likes = models.ManytoMany(User, related_name="likes_questions")


class Answer(modles.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.ForeignKey(Question, null = True)
	author = models.CharField()
