import email
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
               email    = self.normalize_email(email),
               username = username, 
            )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
               email    = self.normalize_email(email),
               password = password,
               username = username,
            ) 
        user.is_admin     = True
        user.is_staff     = True
        user.is_superuser = True
        user.is_employee = True
        user.is_hr        = True
        user.save(using=self.db)
        return user


#Create a custom user

class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username        = models.CharField(max_length=60, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False) 
    is_employee     = models.BooleanField(default=True) 
    is_hr           = models.BooleanField(default=False) 


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin 

    def has_module_perms(self, app_label):
        return True


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Role(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
        return self.name

class Category(models.Model):
     name = models.CharField(max_length=200)

     def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200, null=True)
    employee_id = models.CharField(max_length=200, null=True)
    department = models.ForeignKey (Department, null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey (Role, null=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic =models.ImageField(default="Profile Pic.jpg",null=True, blank=True, upload_to="images/")
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Computer(models.Model):
    serial_no = models.CharField(max_length=200, null=True)
    computer_make = models.CharField(max_length=200, null=True)
    computer_model= models.CharField(max_length=200, null=True)
    ram = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    memory = models.CharField(max_length=200, null=True)
    processor = models.CharField(max_length=200, null=True)
    condition = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=12, null=True)
    photo = models.ImageField(default="Profile Pic.jpg",null=True, blank=True, upload_to="images/")
    comment =  models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.serial_no


class Assign(models.Model):
    employee = models.ForeignKey(Employee, blank=True, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True)
    serial_no = models.OneToOneField(Computer, blank=True, null=True, on_delete=models.PROTECT)
    previous_user = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            Computer.objects.filter(pk=self.serial_no_id).update(status="Assigned" )
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        Computer.objects.filter(pk=self.serial_no_id).update(status="Not Assigned" )
        super().delete(*args, **kwargs)

class ComputerRequest(models.Model):
    new_employee = models.CharField(max_length=200, null=True)
    new_department = models.CharField(max_length=200, null=True)
    new_role = models.CharField(max_length=200, null=True)
    created_by = models.CharField(max_length=50, null=True )
    resumption_date = models.DateField()
    
    def __str__(self):
        return self.new_employee
