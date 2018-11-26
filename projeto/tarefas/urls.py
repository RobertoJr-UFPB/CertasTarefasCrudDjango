
from django.urls import path
from .views import tarefas_list, tarefas_new,tarefas_update, tarefas_delete, home 
urlpatterns = [
	path('', home),
	path('list/', tarefas_list, name="listarTarefas"),
	path('new/', tarefas_new, name="novaTarefa"),
	path('update/<int:id>', tarefas_update, name="atualizaTarefa"),
	path('delete/<int:id>', tarefas_delete, name="deletaTarefa"),
]
