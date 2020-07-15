from django.urls import path
from django.conf.urls import url
from mysite import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import *



urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('inventory/', views.inventory, name='inventory'),
    path('pantries/', views.pantries, name= 'pantries'),
    path('add/', views.add, name= 'add'),
    path('remove/', views.remove, name= 'remove'),
    url (r'^display_food$', display_food, name = 'display_food'),
    url (r'^add_food$', add_food, name = 'add_food'),
    url (r'^edit_food/(?P<pk>\d+)$', edit_food, name = 'edit_food'),
    url (r'^delete_food/(?P<pk>\d+)$', delete_food, name = 'delete_food'),
    url (r'^send_mail$', send_mail, name = 'send_mail'),
    url (r'^send_mail_form$', send_mail_form, name = 'send_mail_form'),
]
