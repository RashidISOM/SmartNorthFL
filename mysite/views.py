from django.shortcuts import render, get_object_or_404, redirect
import re
import sys
from array import *
from .models import Food
from .models import Pantry
from .forms import RegisterForm
from .forms import FoodForm
from .forms import findPantry
from .calc import *
from .forms import *
from django.core.mail import send_mass_mail
from django.http import HttpResponse



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
      i = 0
      order = [[]]
      with  open("zipCodes","r") as conversions:
        for location in listedPantries:
          for line in conversions:
            if re.search('^' + location.getZipCode() + '[,]+[^\n]*$', line):
              print(line)
              line = line.split(",")
              distance = round(calc_dist_fixed(userLat, userLon, float(line[1].strip()), float(line[2].strip())), 2)
              if i == 0:
                order[i] = [distance, location.name, location.zipCode, location.streetAdd1, location.streetAdd2, location.city, location.state, location.phone_number, location.description, location.websiteURL, location.need_set.all, location.hours_set.all, location.id]
                i += 1
              else:
                order.insert(i, [distance, location.name, location.zipCode, location.streetAdd1, location.streetAdd2, location.city, location.state, location.phone_number, location.description, location.websiteURL, location.need_set.all, location.hours_set.all, location.id])
                i += 1
              conversions.seek(0)
              break
      conversions.close()
      for r in order:
        for c in r:
          print(c,end='')
        print()
      order = bubbleSort(order)
      for r in order:
        for c in r:
          print(str(c) + ' ',end='')
        print()
        print()
      return render(request, 'findpantrypage.html', {'listedPantries':listedPantries, 'form':form, 'order':order})
    else:
      i = 0
      order = [[]]
      for location in listedPantries:
        if i == 0:
          order[i] = ['N/A', location.name, location.zipCode, location.streetAdd1, location.streetAdd2, location.city, location.state, location.phone_number, location.description, location.websiteURL, location.need_set.all, location.hours_set.all, location.id] 
          i += 1
        else:
          order.insert(i, ['N/A', location.name, location.zipCode, location.streetAdd1, location.streetAdd2, location.city, location.state, location.phone_number, location.description, location.websiteURL, location.need_set.all, location.hours_set.all, location.id])
        i += 1
      return render(request, 'findpantrypage.html', {'listedPantries':listedPantries, 'form':form, 'order':order})

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
        data = request.POST.copy()
        form = FoodForm (request.POST)
        #print(form.model)

        if form.is_valid():
            food = Food()
            food.Name = data.get('Name')
            food.Status = data.get('Status')
            food.Amount = data.get('Amount')
            for pantry in request.user.pantry_set.all():
              food.Pantry = pantry
              #just gets first pantry for a user becuase each user should only have one pantry
              break
            food.save()
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

def send_mail_form(request):
    users = User.objects.filter(is_active=True).values_list('email', flat=True)
    if request.method == "POST":
        form = mailForm (request.POST)
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')
        if form.is_valid():
            msg1 = (subject, message, 'Techpointteam1nonprofit@gmail.com', ['pbelpasso@hotmail.com'] )
            send_mass_mail((msg1,))         
            return redirect('inventory')
    else:
        form = mailForm()
        return render(request, 'send_mail.html', {'form': form})
    
def add_pantry(request):
    if request.method == "POST":
      form = PantryForm (request.POST)
      data = request.POST.copy()
      if form.is_valid():
        pantry = Pantry()
        pantry.name = data.get('name')
        pantry.zipCode = data.get('zipCode')
        pantry.streetAdd1 = data.get('streetAdd1')
        pantry.streetAdd2 = data.get('streetAdd2')
        pantry.city = data.get('city')
        pantry.state = data.get('state')
        pantry.phone_number = data.get('phone_number')
        pantry.websiteURL = data.get('websiteURL')
        pantry.description = data.get('description')
        pantry.account = request.user.id
        pantry.save()
        return redirect('login')
    else:
        form = PantryForm()
        return render(request, 'addpantry.html', {'form': form})


def edit_pantry(request):
    pantry = get_object_or_404(request.user.pantry_set)
    if request.method == "POST":
        form = PantryForm(request.POST, instance=pantry)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = PantryForm(instance=pantry)

        return render(request, 'editpantry.html', {'form': form})

def about(request):
    return render(request, 'about.html', {})

def sign_up_form(request):
    if request.method == "POST":
      form = donorForm(request.POST)
      if form.is_valid():
        form.save()
        return render(request,'findpantrypage.html')
    else:
        form = donorForm()
        return render(request, 'donor_sign_up.html', {'form': form})
    
def pantry_inventory(request, pantry_id):
  pantry = get_object_or_404(Pantry, pk=pantry_id)
  context = {
        'pantry' : pantry,
  }
  return render (request, 'pantry_inventory.html', context)


##def login(request):
  #  return render(request, 'register/login.html', {})

