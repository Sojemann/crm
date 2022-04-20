from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_employee', 'is_hr')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Employee)
admin.site.register(Computer)
admin.site.register(Assign)
admin.site.register(ComputerRequest)




""" admin.site.register(Account) """