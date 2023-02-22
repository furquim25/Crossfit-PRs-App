from django.shortcuts import render

from core.models import Item

# Create your views here.
def index(request):
     items = Item.objects.all()
     return render(request, 'core/index.html', {
          'items': items
     })
 
def info(request):
    return render(request, 'core/info.html')