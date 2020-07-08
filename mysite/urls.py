from django.urls import path
from mysite import views
from register import views as regView
from django.contrib.auth.views import LoginView
from .views import index



urlpatterns = [
    path('', views.mainpage, name='mainpage'),
#    path('login', views.login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', regView.register, name='register'),
    path('inventory', views.inventory, name='inventory'),
    path('pantries', views.pantries, name= 'pantries'),
    path('add', views.add, name= 'add'),
    path('remove', views.remove, name= 'remove'),
    path('index', views.index, name='index' ),
]
