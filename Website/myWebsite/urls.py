from django.urls import path
from . import views


#Main website
urlpatterns = [
	path("projects/",views.projects, name="projects"), #Leads to the projects function in views.py
	path("",views.home, name="home"), #Leads to the home function in views.py
	path("about/",views.about, name="about"), #Leads to the about page via views.py
]