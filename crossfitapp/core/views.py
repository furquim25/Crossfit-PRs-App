from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from core.models import Item

from .forms import SignupForm, NewItemForm, EditItemForm

# Create your views here.
@login_required
def index(request):
     query = request.GET.get('query','')
     items = Item.objects.filter(created_by=request.user)
     
     if query:
          items = items.filter(name__icontains=query)
     
     return render(request, 'core/index.html', {
          'items': items,
          'query': query
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

@login_required
def new(request):
     if request.method == 'POST':
          form = NewItemForm(request.POST)
          if form.is_valid():
               item = form.save(commit=False)
               item.created_by = request.user
               item.save()
               
               return redirect('/')
     else:
          form = NewItemForm()
     return render(request, 'core/form.html',{
          'form': form,
          'title': 'New Personal Record'
     })
     
@login_required
def edit(request, pk):
     item = get_object_or_404(Item, pk=pk, created_by=request.user)
     
     if request.method == 'POST':
          form = EditItemForm(request.POST, instance=item)
          if form.is_valid():
               form.save()
               
               return redirect('/')
     else:
          form = EditItemForm(instance=item)
     return render(request, 'core/form.html',{
          'form': form,
          'title': 'Edit Personal Record',
          
     })
     
@login_required
def delete(request, pk):
     item = get_object_or_404(Item,pk=pk,created_by=request.user)
     item.delete()
     
     return redirect('core:index')
     