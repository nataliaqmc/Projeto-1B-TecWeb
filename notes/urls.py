from notes.models import Note
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update', views.update),
    path('delete/<int:id>', views.delete),  
    path('tags.html', views.tags),
    path('index.html', views.index),
    path('tagsDetalhadas.html/<str:tagTitle>', views.tagsDetalhadas),
]