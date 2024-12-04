from django.contrib import admin
from django.urls import path
from .views import index, jogadorList, jogadorCreate, jogadorDelete, jogadorUpdate

urlpatterns = [ 
  path('jogador-list', jogadorList, name='jogador-list'),
  path('jogador-create', jogadorCreate, name='jogador-create'),
  path('jogador-delete/<int:idjogador>/', jogadorDelete, name='jogador-delete'),
  path('jogador-update/<int:idjogador>', jogadorUpdate, name='jogador-update'),
  path('index',index, name='index'),
  ]