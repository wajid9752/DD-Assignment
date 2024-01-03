from imports import *

@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def manager_home(request):
    context={
        'teams': Team.objects.filter(manager=request.user).count(),
        'completed_projects': (Project.objects.filter(manager=request.user , is_completed=True).count()),
        'active_projects': (Project.objects.filter(manager=request.user , is_completed=False).count()),
    }
    return render(request,"main/home.html",context)

@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def manager_projects(request):
    context={'projects': Project.objects.filter(manager=request.user).order_by('-created_at')}
    return render(request,"manager/manager-projects.html",context)


@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def manager_team(request):
    context={'teams': Team.objects.filter(manager=request.user)}
    return render(request,"manager/manager-team.html",context)


@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.manager = request.user
            project.save()
            messages.success(request , "Project Added Succesfully")
            return JsonResponse({'status':"success"})
        else:
            return JsonResponse({'status':f'{form.errors}'})
    else:
        form = ProjectForm()
    return render(request, 'manager/add_project.html', {'form': form})


@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            getData= request.POST.getlist("members")
            team = form.save(commit=False)
            team.manager = request.user
            team.save()
            team.members.add(*getData) 
            messages.success(request, "Team Added Successfully")
            return JsonResponse({'status': "success"})
        else:
            return JsonResponse({'status': f'{form.errors}'})
    else:
        form = TeamForm()
    return render(request, 'manager/add-team.html', {'form': form})

@user_passes_test(lambda u: u.role == 'manager', login_url='/login/')
def assign_task(request , project_id , user_id):
    getUser=User.objects.get(id=user_id)
    getProj=Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.manager = request.user
            team.assigned_to = getUser
            team.project = getProj
            team.save()
            messages.success(request, f"Task to {getUser.username} assigned Successfully")
            return JsonResponse({'status': "success"})
        else:
            return JsonResponse({'status': f'{form.errors}'})
        
    context={
        "form" : AddTaskForm(),
        "project_id": project_id,
        "user_id": user_id,
        "quote": f"Assin the task to {getUser.username} for {getProj.name}"
    }
  
    return render(request, 'manager/assign-task.html', context)


###############   Filters ###############

def team_filter(request):
    team_id=request.GET.get('team_id')
    
    if team_id != 'all_team':
        teams   = Team.objects.filter(manager=request.user , id=team_id)

    else:
        teams = Team.objects.filter(manager=request.user)

    return render(request , 'manager/partials/teams.html' , {'teams':teams}  )  
     

