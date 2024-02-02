from django.urls import path
from core.views import (
    OwnerUserListCreate,
    EmployeeUserListCreate,
    EmployeeDesignationListCreate,
    EmployeeDesignationDetails,
    OwnerUserDetails,
    EmployeeUserDetails,
    CustomerUserListCreate,
    CustomerUserDetails,
)

urlpatterns = [
    path('owners/', OwnerUserListCreate.as_view(), name='owner-user-list-create'),
    path('owners/<int:id>/', OwnerUserDetails.as_view(), name='owner-user-details'),
    path('employees/', EmployeeUserListCreate.as_view(), name='employee-user-list-create'),
    path('employees/<int:id>/', EmployeeUserDetails.as_view(), name='employee-user-details'),
    path('customers/', CustomerUserListCreate.as_view(), name='customer-user-list-create'),
    path('customers/<int:id>/', CustomerUserDetails.as_view(), name='customer-user-details'),
    path(
        'employee-designations/',
        EmployeeDesignationListCreate.as_view(),
        name='employee-designation-list-create'
    ),
    path(
        'employee-designations/<int:id>/',
        EmployeeDesignationDetails.as_view(),
        name='employee-designation-details'
    ),
]
