from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"),
    path('about/', views.about, name="about"),
    path('hello/<str:user>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('project_detail/<int:id>', views.projects_detail, name="project_detail"),
    path('task/', views.tasks, name="tasks"),
    path('create_task/', views.create_tasks, name="create_task"),
    path('create_projects/', views.create_projects, name="create_project"),
    
]