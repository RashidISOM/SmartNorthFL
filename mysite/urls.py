from django.urls import path
from django.conf.urls import url
from mysite import views
from django.contrib.auth.views import LoginView
from .views import display_food



urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', views.register, name='register'),
    path('inventory', views.inventory, name='inventory'),
    path('pantries', views.pantries, name= 'pantries'),
    path('add', views.add, name= 'add'),
    path('remove', views.remove, name= 'remove'),
    url (r'^display_food$', display_food, name = 'display_food'),
]
