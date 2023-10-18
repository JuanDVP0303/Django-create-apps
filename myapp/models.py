from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    hours = models.DecimalField(max_digits=30, decimal_places=2, default=2)
    
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title + " - " + self.project.name