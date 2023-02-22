from django.urls import path, re_path
from django.urls.re_path import include, re_path
from mysite import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

# Links button addresses to django views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('inventory/', views.inventory, name='inventory'),
    path('pantries/', views.pantries, name= 'pantries'),
    path('add/', views.add, name= 'add'),
    path('remove/', views.remove, name= 'remove'),
    path('about/', views.about, name='about'),
    re_path (r'^add_pantry$', add_pantry, name = 'add_pantry'),
    re_path (r'^edit_pantry/$', edit_pantry, name = 'edit_pantry'),
    re_path (r'^display_food$', display_food, name = 'display_food'),
    re_path (r'^add_food$', add_food, name = 'add_food'),
    re_path (r'^edit_food/(?P<pk>\d+)$', edit_food, name = 'edit_food'),
    re_path (r'^delete_food/(?P<pk>\d+)$', delete_food, name = 'delete_food'),
    re_path (r'^send_mail_form$', send_mail_form, name = 'send_mail_form'),
    re_path (r'^sign_up_form$', sign_up_form, name = 'sign_up_form'),
    re_path (r'^pantry_inventory/(?P<pantry_id>[0-9]+)$', pantry_inventory, name = 'pantry_inventory'),
    re_path (r'^add_hours$', add_hours, name = 'add_hours'),
    re_path (r'^edit_hours/(?P<pk>\d+)$', edit_hours, name = 'edit_hours'),
    re_path (r'^delete_hours/(?P<pk>\d+)$', delete_hours, name = 'delete_hours'),
    re_path (r'^add_need$', add_need, name = 'add_need'),
    re_path (r'^delete_need/(?P<pk>\d+)$', delete_need, name = 'delete_need'),
]
