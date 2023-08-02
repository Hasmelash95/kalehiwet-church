from django.shortcuts import render, HttpResponse
from django.views import generic, View
from .models import Profile

# Create your views here.

def home_page(request):
    
    return render(request, 'index.html', None)

class MemberProfile(generic.ListView):

    model = Profile
    template_name = 'about.html'
    context_object_name = 'profile'