from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from computers.forms import RegistrationForm, AssignForm, RoleForm, DepartmentForm, EmployeeForm, ComputerRequestForm, ComputerForm, AccountForm
from .models import Account
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.core.mail import send_mail
from django.conf import settings
from .models import *


# Create your views here.

def registration_view(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('index')
        else:
            form = RegistrationForm()
            return render(request,'computers/register.html', {'form': form})

    return render(request,'computers/register.html', {'form': form})

def login_request(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    context = {
        'form': form
    }
    return render(request, 'computers/login.html', context)
    

def logout_request(request):
    logout(request)

    messages.info(request, "Logged out successfully!")
    return redirect('login')


@user_passes_test(lambda u : u.is_admin)
def index(request):
    
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, 'computers/index.html', context)

""" def userCreate(request):
    form = AccountForm()

    if request.method=='POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
    context = {
        'form': form,
        }

    return render(request, 'computers/createuser.html', context) """


@user_passes_test(lambda u : u.is_admin)
def userList(request):
    
    accounts = Account.objects.all()

    context = {
        'accounts': accounts
    }

    return render(request, 'computers/user.html', context)

def userDetails(request, pk):

    account = Account.objects.get(id = pk)

    context = {
        'account': account
    }

    return render(request, 'computers/userdetails.html', context)

def updateUser(request, pk):

    account = Account.objects.get(id=pk)

    form =AccountForm(instance = account)

    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance = account)
        if form.is_valid():
            form.save()
            return redirect('user')

    context = {
        'form': form,
        'account': account
        }

    return render(request, 'computers/updateuser.html', context)


def listGroup(request):
    groups = Group.objects.all()

    context = {
        'groups': groups
    }

    return render(request, 'computers/listgroup.html', context)

# For group feature (Not using it for the project)
def createGroup(request):
    if request.method == 'POST':
      new_group = Group(
          name = request.POST['group_name']
      )
      new_group.save()

      return redirect('listgroup')

    return render(request, 'computers/creategroup.html')

# For group feature (Not using it for the project)
def userGroup(request, pk):
    group = Group.objects.all()

    if request.method == 'POST':

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        user = User.objects.get(id=pk)
        user.groups.add(group)
        return redirect('listuser')
    context ={
        'group': group
    }
    return render(request, 'computers/user_group.html', context)

""" def users_groups(request, pk):
    user = User.objects.get(id=pk)

    ugroup=[]
    for i in user.group.all():
        ugroup.append(i.name)
    context = {
        'user': user,
        'ugroup': ugroup
    }
    return render(request, 'computers/userdetails.html', context ) """
    
@login_required
def index(request):
    assigns = Assign.objects.all()

    laptops = Computer.objects.all()

    all_laptops = laptops.count()

    assigned_laptops = laptops.filter(status="Assigned").count()

    unassigned_laptops = laptops.filter(status="Not Assigned").count()

    """  all_desktops = laptops.filter(Computer.category="Desktop").count() """

    """ all_employees = employees.count() """

    search_input = request.GET.get('name-search')

    if search_input:
        assigns = Assign.objects.filter(employee__name__icontains=search_input)

    else:
        assigns = Assign.objects.all()
        search_input = ''


    context = {
        'assigns': assigns,
        'laptops': laptops,
        'all_laptops': all_laptops,
        'assigned_laptops': assigned_laptops,
        'unassigned_laptops': unassigned_laptops,
        """ 'all_desktops': all_desktops, """
        'search_input': search_input
    }
    return render(request, 'computers/index.html', context)


def createLaptop(request):

    form = ComputerForm()

    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES)

        if form.is_valid():
            computers = Computer(
                serial_no = request.POST['serial_no'],
                computer_make = request.POST['computer_make'],
                computer_model= request.POST['computer_model'],
                ram = request.POST['ram'],
                category = Category.objects.get(id=request.POST['category']),
                memory = request.POST['memory'],
                processor = request.POST['processor'],
                condition = request.POST['condition'],
                status = 'Not Assigned',
                photo = request.FILES['photo'],
                comment =  request.POST['comment'],
            )
            computers.save()
            return redirect('laptop')         

    context = {
        'form': form,
        }

    return render(request, 'computers/createLaptop.html', context)


def laptop(request):
    
    laptops = Computer.objects.all()

    context = {
        'laptops': laptops
    }

    return render(request, 'computers/laptop.html', context)



def updateLaptop(request, pk):

    laptop = Computer.objects.get(id=pk)

    form = ComputerForm(instance = laptop)

    if request.method == 'POST':
        form = ComputerForm(request.POST, request.FILES, instance = laptop)
        if form.is_valid():
            form.save()
            return redirect('laptop')

    context = {
        'form': form,
        'laptop': laptop
        }

    return render(request, 'computers/updatelaptop.html', context)

@user_passes_test(lambda u : u.is_admin)
def assignLaptop(request):

    form = AssignForm()
    employees = Employee.objects.all()
    laptops = Computer.objects.all()

    if request.method == 'POST':
        form = AssignForm(request.POST)

        if form.is_valid():
            assigns = Assign(
                employee = Employee.objects.get(id=request.POST['employee']), 
                email = request.POST['email'], 
                serial_no = Computer.objects.get(id=request.POST['serial_no']), 
                previous_user = request.POST['previous_user']
            )

            form.save()
            return redirect('index')         

    context = {
        'form': form,
        'employees': employees
        }

    return render(request, 'computers/assignlaptop.html', context)

    

def assignDetail(request, pk):

    assign = Assign.objects.get(id=pk)

    context = {
        'assign': assign
    }

    return render(request, 'computers/assigndetail.html', context)


def laptopDetail(request, pk):

    laptop = Computer.objects.get(id=pk)

    context = {
        'laptop': laptop
    }

    return render(request, 'computers/laptopdetail.html', context)


def createRole(request):

    form = RoleForm()

    if request.method == 'POST':
        form = RoleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('role')         

    context = {
        'form': form,
        }

    return render(request, 'computers/createrole.html', context)


def role(request):
    roles = Role.objects.all()

    context = {
        'roles': roles
    }

    return render(request, 'computers/role.html', context)


def createDepartment(request):

    form = DepartmentForm()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)

        if form.is_valid(): 
            try:
               form.save()
               return redirect('department') 
            except:
                pass        
    else:
        form = DepartmentForm()
        
    context = {
        'form': form,
        }

    return render(request, 'computers/createdepartment.html', context)


def department(request):
    departments = Department.objects.all()

    context = {
        'departments': departments
    }

    return render(request, 'computers/department.html', context)

def createEmployee(request):

    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('employee')         

    context = {
        'form': form,
        }

    return render(request, 'computers/createemployee.html', context)


def employee(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }

    return render(request, 'computers/employee.html', context)


def updateEmployee(request, pk):

    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(request.POST, request.FILES, instance = employee)
    if form.is_valid():
        form.save()
        return redirect('employee')

    context = {
        'form': form,
        'employee': employee
        }

    return render(request, 'computers/updateemployee.html', context)


def employeedetail(request, pk):

    employee = Employee.objects.get(id=pk)

    context = {

        'employee': employee
    }

    return render(request, 'computers/employeedetail.html', context)


def createLaptopRequest(request):

    form = ComputerRequestForm()

    if request.method == 'POST':
        form = ComputerRequestForm(request.POST)

        if form.is_valid():

            laptoprequest = ComputerRequest(
            new_employee = request.POST['new_employee'],
            new_department = request.POST['new_department'],
            new_role = request.POST['new_role'],
            created_by = request.user,
            resumption_date = request.POST['resumption_date']
            )
            
            
            new_employee = form.cleaned_data['new_employee']
            new_department = form.cleaned_data['new_department']
            new_role = str(form.cleaned_data['new_role'])
            resumption_date = form.cleaned_data['resumption_date']
             
            subject = "Laptop Request For {form.new_employee}"
            message = "Kindly get a laptop ready for our new staff"

            send_mail( 
                subject, 
                message, 
                settings.EMAIL_HOST_USER, 
                ['itsupport@skld.ng'], 
                fail_silently= False
                )

            
            laptoprequest.save()
            return redirect('index')         

    context = {
        'form': form,
        }

    return render(request, 'computers/laptoprequest.html', context)


def request(request):
    laptoprequests = ComputerRequest.objects.all()

    context = {
        'laptoprequests': laptoprequests
    }

    return render(request, 'computers/request.html', context)


def deleteRole(request, pk):

    role = Role.objects.get(id = pk)

    if request.method == 'POST':
        role.delete()
        return redirect('role')

    context = {'item': role}

    return render(request, 'computers/delete_role.html', context)


def deleteDepartment(request, pk):

    department = Department.objects.get(id = pk)

    if request.method == 'POST':
        department.delete()
        return redirect('/')

    context = {'item': department}

    return render(request, 'computers/delete_department.html', context)


def deleteAssign(request, pk):

    assign = Assign.objects.get(id = pk)

    if request.method == 'POST':
        assign.delete()
        return redirect('index')

    context = {'assign': assign}

    return render(request, 'computers/delete_assign.html', context)


def deleteEmployee(request, pk):

    employee = Employee.objects.get(id = pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee')

    context = {'employee': employee}

    return render(request, 'computers/delete_employee.html', context)


def deleteLaptopRequest(request, pk):

    laptoprequest = ComputerRequest.objects.get(id = pk)

    if request.method == 'POST':
        laptoprequest.delete()
        return redirect('request')

    context = {'laptoprequest': laptoprequest}

    return render(request, 'computers/delete_laptoprequest.html', context)


def deleteLaptop(request, pk):

   laptop = Computer.objects.get(id = pk)

   if request.method == 'POST':
        laptop.delete()
        return redirect('laptop')

   context = {'laptop': laptop}

   return render(request, 'computers/delete_laptop.html', context)


def updateRole(request, pk):

    role = Role.objects.get(id=pk)

    form = RoleForm(instance = role)

    if request.method == 'POST':
        form = RoleForm(request.POST, instance = role)
        if form.is_valid():
            form.save()
            return redirect('role')

    context = {
        'form': form,
        'role': role
        }

    return render(request, 'computers/updaterole.html', context)


def updateDepartment(request, pk):

    department = Department.objects.get(id=pk)

    form = DepartmentForm(instance = department)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance = department)
        if form.is_valid():
            form.save()
            return redirect('department')

    context = {
        'form': form,
        'department':department
        }

    return render(request, 'computers/updatedepartment.html', context)


def updateEmployee(request, pk):

    employee = Employee.objects.get(id=pk)

    form = EmployeeForm(instance = employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            form.save()
            return redirect('employee')

    context = {
        'form': form,
        'employee': employee
        }

    return render(request, 'computers/updateemployee.html', context)

