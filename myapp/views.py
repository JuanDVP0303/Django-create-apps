from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateTask, CreateProjectFrom
# Create your views here.
def hello(request,user):
    return HttpResponse("<h1>Hello %s!</h1> " % user )

def about(request):
    return render(request, "about.html")


def main(request):
    title = "Welcome to battle royale!!"
    return render(request, "index.html", {
        "title" : title
    })
def projects(request):
    projects = Project.objects.all()
    return render(request,"projects/projects.html", {"projects":projects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request,"task/task.html", {"tasks":tasks})
    
    # task = get_object_or_404(Task, project_id=project_id)
    # return HttpResponse("<h2>Your task is: %s</h2>" % task.title)


def create_tasks(request):
    # print(len(Project.objects.all()))
    if len(Project.objects.all()) == 0:
        return redirect("create_project")
    if request.method == "GET" :
        return render(request, "task/create_task.html",{
        "forms":CreateTask()
    })
    else:
        Task.objects.create(title = request.POST["title"], description = request.POST["description"], project_id = request.POST["projectRelated"])

        return redirect("tasks")
     
    
def create_projects(request):
    if request.method == "GET":
        return render(request, "projects/create_projects.html",{
            "form" : CreateProjectFrom()
        })
    else:
        Project.objects.create(name=request.POST["name"], hours=request.POST["hours"])
        return redirect("projects")
    
    
def projects_detail(request,id):
    project = Project.objects.get(id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "projects/project_detail.html",{
        "project":project,
        "tasks": tasks
    })