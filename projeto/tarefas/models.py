from django.db import models

# Create your models here.
class Tarefa(models.Model):
	titulo = models.CharField(max_length=20)
	descricao = models.TextField()
	def __str__(self):
		return self.titulo