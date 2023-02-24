from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView,DetailView
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def index(request):
	return render(request,'index.html')

class PortfolioView(TemplateView):
	template_name="olatidejoseph.html"

class IndexListView(ListView):
	template_name="index.html"
	model=Post
class BlogDetailView(DetailView):
	model=Post
	template_name="blog/full_post.html"