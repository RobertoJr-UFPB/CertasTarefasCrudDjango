from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa 
from .forms import TarefaForm
# Create your views here.

def home(request):
	return render(request, 'home.html')

def tarefas_list(request):
	tarefa = Tarefa.objects.all()
	return render(request, 'list.html', {'Tarefa':tarefa})

def tarefas_new(request):
	form = TarefaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('listarTarefas')
	return render(request,'cadastro.html',{'form':form})

def tarefas_update(request, id):
	tarefa = get_object_or_404(Tarefa, pk= id)
	form = TarefaForm(request.POST or None, instance= tarefa )
	if form.is_valid():
		form.save()
		return redirect('listarTarefas')
	return render(request, 'editar.html', {'form':form})

def tarefas_delete(request, id):
	tarefa = get_object_or_404(Tarefa, pk= id)
	#form = TarefaForm(request.POST or None, instance= tarefa )
	if request.method == 'POST':
		tarefa.delete()
		return redirect('listarTarefas')
	return render(request, 'confirmDelete.html', {'tarefa':tarefa})