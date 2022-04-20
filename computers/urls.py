from django.urls import path
from django.contrib.auth import views as auth_views 
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="computers/password_reset.html"), 
        name='reset_password'),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="computers/password_reset_sent.html"), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="computers/password_reset_form.html"), 
        name='password_reset_confirm'),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="computers/password_reset_done.html"), 
        name='password_reset_complete'),
  
    path('user/', views.userList, name='user'),
    path('userdetails/<str:pk>/', views.userDetails, name='userdetails'),
    path('updateuser/<str:pk>/', views.updateUser, name='updateuser'),
    path('usergroup/<str:pk>/', views.userGroup, name='usergroup'),


    path('listgroup/', views.listGroup, name='listgroup'),
    path('creategroup/', views.createGroup, name='creategroup'),

    path('assigndetail/<str:pk>/', views.assignDetail, name='assigndetail'),
    path('laptopdetail/<str:pk>/', views.laptopDetail, name='laptopdetail'),
    path('employeedetail/<str:pk>/', views.employeedetail, name='employeedetail'),

    path('assignlaptop/',views.assignLaptop, name='assignlaptop'),
    path('role/',views.role, name='role'),
    path('department/',views.department, name='department'),
    path('employee/',views.employee, name='employee'),
    path('request/',views.request, name='request'),
    path('laptop/',views.laptop, name='laptop'),
    path('laptoprequest/',views.createLaptopRequest, name='laptoprequest'),


    path('createrole/',views.createRole, name='createrole'),
    path('createdepartment/',views.createDepartment, name='createdepartment'),
    path('createemployee/',views.createEmployee, name='createemployee'),
    path('createlaptop/',views.createLaptop, name='createlaptop'),

    path('updateemployee/<str:pk>/',views.updateEmployee, name='updateemployee'),
    path('updatelaptop/<str:pk>/',views.updateLaptop, name='updatelaptop'),
    path('updatedepartment/<str:pk>/',views.updateDepartment, name='updatedepartment'),
    path('updaterole/<str:pk>/',views.updateRole, name='updaterole'),


    path('deletelaptop/<str:pk>/',views.deleteLaptop, name='deletelaptop'),
    path('deleteassign/<str:pk>/',views.deleteAssign, name='deleteassign'),
    path('deleterole/<str:pk>/',views.deleteRole, name='deleterole'),
    path('deletedepartment/<str:pk>/',views.deleteDepartment, name='deletedepartment'),
    path('deletelaptoprequest/<str:pk>/',views.deleteLaptopRequest, name='deletelaptoprequest'),
    path('deleteemployee/<str:pk>/',views.deleteEmployee, name='deleteemployee'),

]

