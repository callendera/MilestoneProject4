from django.shortcuts import render

def index(request):
    """A view that displays index page"""
    return render(request, "index.html")