from django.shortcuts import render, HttpResponse

# Create your views here.

def views_test(request):
    return HttpResponse("Does this work?")