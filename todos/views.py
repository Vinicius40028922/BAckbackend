from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo    

def home(request):
    return render(request, "todos/home.html")

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos":todos})

def todo_list_old(request):
    nome = 'Rodrigo'
    alunos = ['1.Ana', '2.José', '3.Bia']
    return render(request, "todos/todo_list.html", {"nome":nome, "lista_alunos":alunos})




# Create your views here.
