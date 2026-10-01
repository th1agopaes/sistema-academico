from django.urls import path

from estudantes import views

urlpatterns = [
    path('', views.listarEstudantes, name ='listagem'),
    path('editar/<id>', views.atualizarEstudante, name = 'editar'),
    path('adicionar/', views.criarEstudante, name = 'adicionar'),
    path('deletar/<id>', views.deletarEstudante, name='deletar'),
]