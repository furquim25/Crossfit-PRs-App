from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout

from core.models import Item

from .forms import SignupForm

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
     
def signup(request):
     if request.method == "POST":
          form = SignupForm(request.POST)
          if form.is_valid():
               form.save()
               print('is valid')
               return redirect('/login/')
     else:
          form = SignupForm()
     return render(request, 'core/signup.html', {
          'form': form
     })

def logout_view(request):
     logout(request)
     print("LOGOUT")
     return redirect('/login/')