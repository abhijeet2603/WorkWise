from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from EmpApp.models import Employee


# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        new_emp = Employee(First_Name=first_name, Last_Name=last_name, Dept_id=dept, Phone=phone, Salary=salary, Bonus=bonus, Role_id=role, HireDate=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Exception: Employee Has Not Been Added")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_romoved = Employee.objects.get(id=emp_id)
            emp_to_be_romoved.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid Employee Id")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(First_Name__icontains=name) | Q(Last_Name__icontains=name))
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse("Please Enter A Valid Detail")
