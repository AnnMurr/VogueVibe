from django.shortcuts import render

# Create your views here.


def catalog(request):
    context = {
       'title': 'Vogue Vibe',
       'goods': [
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
           {
               'image': 'deps/images/t-shirt.jpeg',
               'name': 'T-shirt',
               'price': 14.99
           },
       ] 
    }
    return render(request, "goods/catalog.html", context)
    
def product(request):
    render()