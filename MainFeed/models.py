from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=settings.USER_LENGTH)
	password = models.CharField(max_length=50)
	num_followers = models.IntegerField(default=0)
	num_following = models.IntegerField(default=1)
	followers = models.CharField(max_length = 1000) #	This will have to change if the platform ever gets big
	following = models.CharField(max_length = 1000)
	join_date = models.DateTimeField('DATE JOINED')
	def __str__(self):
		return self.username
class Post(models.Model):
	image_url = models.CharField(max_length=1000)
	post_description = models.CharField(max_length=1000)
	tags = models.CharField(max_length=1000) #	<-- Will work on this later
	mentions = models.CharField(max_length = 1000)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	creation_date = models.DateTimeField('DATE CREATED')
	likes = models.IntegerField(default=0)
	flags = models.IntegerField(default=0)
	def __str__(self):
		return self.post_description;
class Like(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	like_date = models.DateTimeField('DATE LIKED')
class Comment(models.Model):
	tags = models.CharField(max_length=1000) #	<-- Will work on this later
	mentions = models.CharField(max_length=1000)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	creation_date  = models.DateTimeField('DATE COMMENTED')
class Flag(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	reason = models.CharField(max_length = 200)