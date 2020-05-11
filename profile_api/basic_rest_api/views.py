from django.shortcuts import render, HttpResponse, render

# Create your views here.

def index(request):
    return render(request, 'index.html', {})