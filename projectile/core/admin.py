from django.contrib import admin

from common.admin import BaseModelAdmin

from core.models import User, EmployeeDesignation


admin.site.register(User)
class UserAdmin(BaseModelAdmin):
    pass


admin.site.register(EmployeeDesignation)
class EmployeeDesignationAdmin(BaseModelAdmin):
    pass
