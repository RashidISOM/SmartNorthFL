from django.urls import path
from django.conf.urls import url
from mysite import views
from register import views as regView
from django.contrib.auth.views import LoginView
from .views import *



urlpatterns = [
    path('', views.mainpage, name='mainpage'),
#    path('login', views.login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', regView.register, name='register'),
    path('inventory', views.inventory, name='inventory'),
    path('pantries', views.pantries, name= 'pantries'),
    path('add', views.add, name= 'add'),
    path('remove', views.remove, name= 'remove'),
    url (r'^display_food$', display_food, name = 'display_food'),
    url (r'^add_food$', add_food, name = 'add_food'),
    url (r'^edit_food$', edit_food, name = 'edit_food'),
    url (r'^delete_food/(?P<pk>\d+)$', delete_food, name = 'delete_food'),
]
