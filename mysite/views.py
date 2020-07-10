from django.shortcuts import render, redirect
from .models import Food
from .models import Pantry
from .forms import RegisterForm
from .filter import PantryFilter

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html', {})

def inventory(request):
    return render(request, 'inventorypage.html', {})

def pantries(request):
    listedPantries = Pantry.objects.all()
    myFilter = PantryFilter(request.GET, queryset=listedPantries)
    listedPantries = myFilter.qs
    return render(request, 'findpantrypage.html', {'listedPantries':listedPantries, 'myFilter':myFilter})

def add(request):
    return render(request, 'additemspage.html', {})

def remove(request):
    return render(request, 'removeitemspage.html', {})

def display_food(request):
    items = Food.objects.all()
    context = {
        'items' : items,
    }
    return render(request, 'inventorypage.html', context)


def register(response):
   if response.method == "POST":
      form = RegisterForm(response.POST)
      if form.is_valid():
        form.save()
      return redirect("/")
   else:
      form = RegisterForm()

   return render(response, "register/register.html", {"form":form})
