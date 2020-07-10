from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .models import Pantry
from .forms import RegisterForm
from .filter import PantryFilter
from .forms import FoodForm



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

def add_food(request):
    if request.method == "POST":
        form = FoodForm (request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = FoodForm()
        return render(request, 'additemspage.html', {'form': form})

def edit_food(request, pk):
    item = get_object_or_404(Food, pk=pk)

    if request.method == "POST":
        form = FoodForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = FoodForm(instance=item)

        return render(request, 'edit_item.html', {'form': form})
    
def delete_food(request,pk):
    Food.objects.filter(id=pk).delete()
    items = Food.objects.all()
    context = {
        'items':items
    }
    return render(request, 'inventorypage.html', context)

##def login(request):
  #  return render(request, 'register/login.html', {})

