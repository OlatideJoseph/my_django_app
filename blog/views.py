from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def index(request):
	return render(request,'index.html')

def portfolio(request):
	return render(request,"olatidejoseph.html")

class IndexListView(ListView):
	template_name="index.html"
	model=Post