from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	"""Post object from the django model"""
	title=models.CharField(max_length=200)
	text=models.TextField(unique=True)
	author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
	def __str__(self):
		return self.text[:50]
	def get_absolute_url(self):
		return reverse('post_details',kwargs={'pk':self.pk})