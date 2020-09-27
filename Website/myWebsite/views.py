from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(response):
	return render(response, "myWebsite/home.html", {})

def about(response):
	return render(response, "myWebsite/about.html", {})

def projects(response):
	return render(response, "myWebsite/projects.html", {})

#def inprogress(response):
#	return render(response, "myWebsite/in-progress.html", {})