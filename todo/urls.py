from . import views
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.log_in),
    path('todo', views.todo),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('signout/', views.signout, name='signout'),
    
]