from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
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
class BlogCreateView(CreateView):
	model=Post
	template_name="blog/post_create.html"
	fields=['title','author','text']

class BlogUpdateView(UpdateView):
	template_name='blog/post_edit.html'
	model=Post
	fields=['title','text']

class BlogDeleteView(DeleteView):
	model=Post
	template_name='blog/post_delete.html'
	success_url=reverse_lazy('index')