from django.db import models
from django.db.models import Model

class Department(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class ERole(models.Model):
    Name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.Name

# Create your models here.
class Employee(models.Model):
    First_Name = models.CharField(max_length=100, null=False)
    Last_Name = models.CharField(max_length=100)
    Dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    Salary = models.IntegerField(default=0)
    Bonus = models.IntegerField(default=0)
    Role = models.ForeignKey(ERole, on_delete=models.CASCADE)
    Phone = models.IntegerField(default=0)
    HireDate = models.DateField()

    def __str__(self):
        return "%s %s" %(self.First_Name, self.Last_Name)



