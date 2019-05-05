from . import  views
from django.urls import path

urlpatterns = [

    path('register/',views.index,name='index'),
    path('login/',views.Login,name='login')

]