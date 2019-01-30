from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
descriptions, usernames,images = [], [],[]
def index(request):
	global descriptions, usernames,images
	latest_posts = Post.objects.order_by('-creation_date')[:5]
	for post in latest_posts:
		usernames.append(post.author)
		print(post.author)
		images.append(post.image_url)
		descriptions.append(post.post_description)
	details = zip(usernames, latest_posts, descriptions, images)	
	return render(request, 'index.html', {'details': details} )
