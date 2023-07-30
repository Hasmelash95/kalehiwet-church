from django.shortcuts import render, HttpResponse
from django.views import generic, View

# Create your views here.

def home_page(request):
    
    return render(request, 'index.html', None)