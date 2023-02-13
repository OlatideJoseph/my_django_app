from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def index(request):
	return render(request,'index.html')

def portfolio(request):
	return render(request,"olatidejoseph.html")