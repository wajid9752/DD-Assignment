from imports import *

@user_passes_test(lambda u: u.role == 'admin', login_url='/login/')
def users_view(request):
    context={'users':User.objects.all().order_by('-created_at')}
    return render(request , "admins/users.html" , context)



@user_passes_test(lambda u: u.role == 'admin', login_url='/login/')
def admin_home(request):
    context={
        'employees': User.objects.filter(role__in=['employee','manager']).count(),
        'completed_projects': (Project.objects.filter(is_completed=True).count()),
        'active_projects': (Project.objects.filter(is_completed=False).count()),
    }
    return render(request,"main/home.html",context)



@user_passes_test(lambda u: u.role == 'admin', login_url='/login/')
def add_employee(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , "Employee Added Succesfully")
            return JsonResponse({'status':"success"})
        else:
            return JsonResponse({'status':f'{form.errors}'})

    form = UserForm()
    context={'form':form}
    return render(request , "admins/add-employee.html" , context)


@user_passes_test(lambda u: u.role == 'admin', login_url='/login/')
def projects_view(request):
    context={'projects':Project.objects.all()}
    return render(request , "admins/projects.html" , context)



#########################   Filtration ####################


def filterd_users(request):
    status = request.GET.get('users_status')
    if status=="active":
        users = User.objects.filter(active = True ).order_by('-created_at')
    elif status=="deactive":
        users = User.objects.filter(active = False ).order_by('-created_at')
    else:
        users = User.objects.all().order_by('-created_at')
    return render(request , 'admins/partials/users.html' , {'users':users})


def filterd_projects(request):
    admin_status = request.GET.get('projects_status')
    manager_projects = request.GET.get('manager_projects')

    if admin_status != None:
        if admin_status=="active":
            projects =Project.objects.filter(is_completed = True ).order_by('-created_at')
        elif admin_status=="deactive":
            projects = Project.objects.filter(is_completed = False ).order_by('-created_at')
        else:
            projects = Project.objects.all().order_by('-created_at')
        
    elif manager_projects != None:
        if manager_projects == "active":
            projects = Project.objects.filter(manager=request.user , is_completed=True).order_by('-created_at')
        elif manager_projects == "deactive":
            projects = Project.objects.filter(manager=request.user , is_completed = False ).order_by('-created_at')    
        else:
            projects=Project.objects.filter(manager=request.user).order_by('-created_at')
        
    return render(request , 'admins/partials/projects.html' , {'projects':projects})

