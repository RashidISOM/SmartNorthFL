from django.shortcuts import render, get_object_or_404, redirect
import re
import sys
from .models import Food
from .models import Pantry
from .forms import RegisterForm
from .forms import FoodForm
from .forms import findPantry
from .calc import calc_dist_fixed



# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html', {})

def inventory(request):
    return render(request, 'inventorypage.html', {})

def pantries(request):
    form = findPantry()
    listedPantries = Pantry.objects.all()
    if str(request).find('=') != -1:
      userZip = str(request)
      userZip = userZip[userZip.rfind('=')+1:-2]
      with  open("zipCodes","r") as conversions:
        for l in conversions:
          if re.search('^' + userZip + '[,]+[^\n]*$', l):
            print(l)
            l = l.split(",")
            userLat = float(l[1].strip())
            userLon = float(l[2].strip())
            print(userLat)
            print(userLon)
            break
      with  open("zipCodes","r") as conversions:
        for location in listedPantries:
          for line in conversions:
            if re.search('^' + location.getZipCode() + '[,]+[^\n]*$', line):
              print(line)
              line = line.split(",")
              location.setDistance(round(calc_dist_fixed(userLat, userLon, float(line[1].strip()), float(line[2].strip())), 2))
              conversions.seek(0)
              break
      conversions.close()
      #listedPantries = listedPantries.order_by("distance")
    return render(request, 'findpantrypage.html', {'listedPantries':listedPantries, 'form':form})

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
      return redirect("login")
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

