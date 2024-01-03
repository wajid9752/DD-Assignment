from django.urls import path
from .views import *
app_name="manager"
urlpatterns=[
    path('manager-home/' , manager_home , name="manager-home"),
    path('manager-team/' , manager_team , name="manager-team"),
    path('manager-projects/' , manager_projects , name="manager-projects"),
    path('add-project/' , add_project , name="add-project"),
    path('add-team/' , add_team , name="add-team"),
    path('team-filter/' , team_filter , name="team-filter"),
    path('assign-task/<int:project_id>/<int:user_id>/' , assign_task , name="assign-task"),
]
