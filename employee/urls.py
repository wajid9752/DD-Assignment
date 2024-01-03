from django.urls import path
from .views import *
app_name="employee"

urlpatterns=[

    path("employee-home/" , employee_home , name="employee-home"),
    path("employee-task/" , employee_task , name="employee-task"),
    path("employee-filterd/" , employee_filtered , name="employee-filterd"),
    path("update-task/<int:pk>/" , update_task , name="update-task"),
]
