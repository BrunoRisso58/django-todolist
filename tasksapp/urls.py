from django.urls import path
from . import views

# URLConf
urlpatterns = [
	path('', views.home_page),
	path('cadastro/', views.register_task),
 	path('tarefas/', views.all_tasks)
]