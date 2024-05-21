from django.shortcuts import render

# Create your views here.

# Adding home page 
def home(request):
    return render(request, 'base/home.html')