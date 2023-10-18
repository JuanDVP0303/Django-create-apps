from django import forms
from .models import Project

project_query = Project.objects.all()
initial_project = None
if project_query.exists():
    initial_project = Project.objects.all()[0].id


class CreateTask(forms.Form):
    projectRelated = forms.ModelChoiceField(queryset=Project.objects.all(), label="Ingrese el proyecto al que va la tarea", initial=initial_project) 
    
    title = forms.CharField(label="Nombre de tarea", widget=forms.TextInput(attrs={"class":"create-title"}))
    description = forms.CharField(label="Descripción de la tarea", widget=forms.Textarea(attrs={"class":"create-task-description"}))
    
class CreateProjectFrom(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
    hours = forms.IntegerField(label="Horas previstas del proyecto", max_value=500)