from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Todo
from .forms import TodoForm


def create_todo(request):
    if request.method == "GET":
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        pass


def todo_detail(request):
    pass


def all_todos(request):
    todos = Todo.objects.all()
    if todos is None:
        return render(request, 'todo/currenttodos.html', {'message': 'Запланированных дел пока нет'})
    else:
        return render(request, 'todo/currenttodos.html', {'todos': todos})


def login_user(request):
    if request.method == "GET":
        return render(request, "todo/login.html", {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "todo/login.html",
                          {'form': AuthenticationForm(), 'error': 'Неверный логин или пароль'})
        else:
            login(request, user)
            return redirect('all_todos')


def signup_user(request):
    if request.method == "GET":
        return render(request, "todo/signup.html", {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, "todo/signup.html",
                              {'form': UserCreationForm(), 'error': 'Пользователь с таким ником уже существует'})
        else:
            return render(request, "todo/signup.html", {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def currenttodos(request):
    return render(request, "todo/currenttodos.html")


def home(request):
    return render(request, 'todo/home.html')
