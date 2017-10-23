from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Network(models.Model):
    description = models.CharField(max_length=40)
    code = models.CharField(max_length=12)

class ProjectType(models.Model):
    description = models.CharField(max_length=50)
    code = models.CharField(max_length=6)

class ProjectStatus(models.Model):
    description = models.CharField(max_length=40)
    code = models.SmallIntegerField()

class Project(models.Model):
    project_code = models.CharField(max_length=10)
    project_description = models.CharField(max_length=50)
    project_manager = models.OneToOneField(User)
    project_type = models.OneToOneField(ProjectType)
    project_network = models.ForeignKey(Network)
    project_status = models.OneToOneField(ProjectStatus)
    project_startdate = models.DateField()
    project_enddate = models.DateField()
    project_week_number =models.SmallIntegerField()
    project_location = models.CharField(max_length=50)
    project_actual_cost = models.DecimalField(max_digits=10,decimal_places=2)
    project_actual_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    project_actual_pgm = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.project