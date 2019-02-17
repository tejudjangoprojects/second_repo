from django.shortcuts import render
from testapp.forms import EmployeeForm
from testapp.models import Employee

# Create your views hereself.
def display_view(request):
    emp_list=Employee.objects.all()
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('total form validation success and printing the data:')
            print('name:',form.cleaned_data['ename'])
            print('number:',form.cleaned_data['eno'])
            print('esalary:',form.cleaned_data['esal'])
            print('eaddress:',form.cleaned_data['eaddr'])
    return render(request,'testapp/display.html',{'form':form,'emp_list':emp_list})
def data_view(request):
    emp_list=Employee.objects.all()
    return render(request,'testapp/data.html',context={'emp_list':emp_list})
