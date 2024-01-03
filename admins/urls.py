from django.urls import path
from .views import *
app_name="admins"
urlpatterns=[
    path('admin-home/' , admin_home , name="admin-home"),
    path('users-view/' , users_view , name="users-view"),
    path('add-employee/' , add_employee , name="add-employee"),
    path('projects-view/' , projects_view , name="projects-view"),
    path('filterd-users/' , filterd_users , name="filterd-users"),
    path('filterd-projects/' , filterd_projects , name="filterd-projects"),
]
