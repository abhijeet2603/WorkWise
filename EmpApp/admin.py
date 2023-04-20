from django.contrib import admin

from EmpApp.models import Employee, ERole, Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(ERole)
admin.site.register(Department)
