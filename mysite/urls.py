from django.urls import path
from mysite import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login/', LoginView.as_view(), name='login'),

]
