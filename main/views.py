from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    categories = Categories.objects.all()
    
    context={
        'title': 'Vogue Vibe',
        'banner_title': 'City Diaries',
        'banner_subtitle': 'Summer style',
        'banner_button': 'See collection',
        'categories': categories  
    }
    return render(request, "main/index.html", context)

def about(request):
    context = {
         'title': 'Vogue Vibe',
    }
    return render(request, "main/about.html", context)

def career(request):
    context = {
         'title': 'Vogue Vibe',
    }
    return render(request, "main/career.html", context)

def privacy(request):
    context = {
         'title': 'Vogue Vibe',
    }
    return render(request, "main/privacy.html", context)

def terms(request):
    context = {
       'title': 'Vogue Vibe', 
    }
    return render(request, "main/terms.html", context)

def cookies(request):
    context = {
       'title': 'Vogue Vibe', 
    }
    return render(request, "main/cookies.html", context)