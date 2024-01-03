from imports import *


@user_passes_test(lambda u: u.role == 'employee', login_url='/login/')
def employee_home(request):
    context={
        'active_tasks': Task.objects.filter(assigned_to=request.user , status="Pending").count(),
        'completed_tasks': Task.objects.filter(assigned_to=request.user,status="Completed").count()
    }
    return render(request,"main/home.html",context)


@user_passes_test(lambda u: u.role == 'employee', login_url='/login/')
def employee_task(request):
    context={
        'tasks': Task.objects.filter(assigned_to=request.user)
    }
    return render(request,"employee/tasks.html",context)



@user_passes_test(lambda u: u.role == 'employee', login_url='/login/')
def update_task(request,pk):
    obj=Task.objects.get(id=pk)
    form = TaskForm(instance=obj)
    if request.POST:
        form = TaskForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request , f"{request.user.username} Status Updated Successfully")
            return redirect("employee:employee-task")
    context={'form':form , 'title':obj.title}
    return render(request,"employee/update-task.html",context)


def employee_filtered(request):
    get_status = request.GET.get('status', 'all_status')
    get_priority = request.GET.get('priority', 'all_priority')
    tasks = Task.objects.filter(assigned_to=request.user)
    if get_status != 'all_status':
        tasks = tasks.filter(status=get_status)

    if get_priority != 'all_priority':
        tasks = tasks.filter(priority=get_priority)

    return render(request, 'employee/partials/tasks.html', {'tasks': tasks})





