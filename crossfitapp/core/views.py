from django.shortcuts import render, get_object_or_404

from core.models import Item

# Create your views here.
def index(request):
     items = Item.objects.all()
     return render(request, 'core/index.html', {
          'items': items
     })
 
def info(request):
    return render(request, 'core/info.html')

def detail(request, pk):
     item = get_object_or_404(Item, pk=pk)
     return render(request, 'core/details.html',{
          'item': item
     })