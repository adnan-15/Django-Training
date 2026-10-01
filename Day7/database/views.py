from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from database.models import Employee
from django.urls import reverse

def newEmployeeForm(request):
    res=render(request,'newEmployeeForm.html')
    return res

# Create your views here.
def saveuser(request):                     #create record , c of crud
    e_no = request.POST['e_no']
    e_name = request.POST['e_name']
    e_salary = request.POST['e_salary']
    employee = Employee(e_no=e_no, e_name=e_name, e_salary=e_salary)
    employee.save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)
    #

def employeelist(request):                  #read record , r of crud
    Employees=Employee.objects.all()        #it returns query set of enmplyee object
    res=render(request,'employeelist.html',{'Employees':Employees})
    return res

def updateEmployeeform(request):
    id = request.GET['id']
    employee = Employee.objects.filter(id=id).values()
    res=render(request,'updateEmployeeForm.html',{'employee':employee[0]})
    return res

def updateEmployee(request):                #update record , u of crud
    id=request.POST['id']
    e_no = request.POST['e_no']
    e_name = request.POST['e_name']
    e_salary = request.POST['e_salary']
    Employee(id=id,e_no=e_no, e_name=e_name, e_salary=e_salary).save()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)

def deleteEmployee(request):                     #delete record , d of crud
    id=request.GET['id']
    emp=Employee.objects.filter(id=id)
    emp.delete()
    url=reverse('employeelist')
    return HttpResponseRedirect(url)
    
