from fileinput import FileInput
from operator import imatmul
from tkinter import Image
from typing import ClassVar
from django.db.models import fields
from django.forms import CheckboxInput, ClearableFileInput, DateInput, ImageField, ModelForm, TextInput, EmailInput, Select, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms
from .models import *



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Require, add a valid email')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields =['email', 'username', 'is_admin', 'is_active', 'is_staff', 'is_employee', 'is_hr']

class AssignForm(ModelForm):
    class Meta:
        model = Assign
        fields = '__all__'
        """ exclude = ['employee'] """

        widgets = {
            'employee': Select(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Employee'
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Email'
                }),
            'serial_no': Select(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Serial Number'
                }),
            'previous_user': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter previous user'
                }),
        }

class RoleForm(ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Role..'
                }),
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Department..'
                }),
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
           
            'name': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Name..'
                }),
            
            'employee_id': TextInput(attrs={
                'class': "form-control",
               """  'style': 'max-width: 300px;', """
                'placeholder': 'Enter Employee ID..'
                }),
            'department': Select(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Department..'
                }),
            'role': Select(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Email..'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Email..'
                }),
            'phone': TextInput(attrs={
                'class': "form-control",
               """  'style': 'max-width: 300px;', """
                'placeholder': 'Enter Phone No..'
                }),   
            'is_admin': CheckboxInput(), 
            'is_hr': CheckboxInput(), 
        }

class ComputerRequestForm(ModelForm):
    class Meta:
        model = ComputerRequest
        fields = ['new_employee', 'new_department', 'new_role', 'resumption_date']

        widgets = {
            'new_employee': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter New Employee..'
                }),
            'new_department': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Department..'
                }),
            'new_role': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Role..'
                }),
            'resumption_date': DateInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Resumption date.',
                'type': 'date'
                }),
        }

class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = ['serial_no', 'computer_make', 'computer_model', 'ram', 'category', 'memory', 'processor', 'condition', 'photo', 'comment']

        widgets = {
            'serial_no': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Serial Number..'
                }),
            'computer_make': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer Make..'
                }),
            'computer_model': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer Model..'
                }),
            'ram': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer RAM..',
                
                }),
            'category': Select(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer category..',
                
                }),
            'memory': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer Memory..',
                
                }),
            'processor': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer Processor..',
                
                }),
            'condition': TextInput(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Computer Condition..',
                
                }),
            'comment': Textarea(attrs={
                'class': "form-control",
                """ 'style': 'max-width: 300px;', """
                'placeholder': 'Enter Comment..',
                
                }),
        }