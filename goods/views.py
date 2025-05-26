from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
       'title': 'Vogue Vibe', 
    }
    return render(request, "goods/catalog.html", context)
    
def product(request):
    render()