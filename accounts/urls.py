from django.urls import path
from . import views

urlpatterns = [
       path('register/',views.register,name ='register'),
       path('dashboard/',views.profile,name ='profile'),
       path('signin/',views.signIn ,name ='signin'),
    
]