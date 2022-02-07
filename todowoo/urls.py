from django.contrib import admin
from django.urls import path, include
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # авторизация
    path('signup/', views.signup_user, name='signup_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.login_user, name='login_user'),
    # todos
    path('current/', views.all_todos, name='all_todos'),
    path('', views.home, name='home'),
    path('todo/', views.todo_detail, name='todo_detail'),
    path('createtodo/', views.create_todo, name='create_todo'),
]
