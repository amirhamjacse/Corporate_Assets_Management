from django.urls import path
from .views import (
    CompanyCreateViewAPI,
    CompanyListViewAPI,
    CompanyUpdateViewAPI,
    EmployeeAPI

)

urlpatterns = [

    path('api/company/create/',
         CompanyCreateViewAPI.as_view(),
         name='company_creatr'
        ),
    path('api/company/list/',
         CompanyListViewAPI.as_view(),
         name='company_lists'
        ),
    path('api/company/update/<int:pk>/',
         CompanyUpdateViewAPI.as_view(),
         name='company_update'
        ),
    path('api/employee/',
         EmployeeAPI.as_view(),
         name='employee'
        ),
    path('api/employee/<int:pk>/',
         EmployeeAPI.as_view(),
         name='employee_update'
        ),

]