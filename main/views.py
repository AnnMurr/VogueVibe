from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'title': 'Vogue Vibe',
        'banner_title': 'City Diaries',
        'banner_subtitle': 'Summer style',
        'banner_button': 'See collection',
        
    }
    return render(request, "main/index.html", context)

def about(request):
    return render(request, "main/about.html")
