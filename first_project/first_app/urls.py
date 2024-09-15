from django.urls import path
from .views import store_book,show_book,edit_book,delet_book
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('singup/', views.singup, name='singup'),
    path('login/', views.loginn, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('passchange/', views.pass_change, name='passchange'),
    #path('passchange2/', views.pass_change2, name='passchange2'),
    path('profile/', views.profile, name='profile'),
    path('changeprofile/', views.change_profile, name='changeprofile'),
    path('home1/', views.home1, name='home1'),
    path('store_new_car/',store_book, name='storebook'),
    path('show_car/',show_book, name='showbook'),
    path('edit_book/<int:id>',edit_book, name='edit_book'),
     path('delet_book/<int:id>',delet_book, name='delet_book'),
]
