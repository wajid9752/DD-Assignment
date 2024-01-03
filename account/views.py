from imports import *

@login_required(login_url="account:login")
def home(request):
    
    # if user is admin it will be redirectto admin-home page that is located in admins app 
    if request.user.role == "admin":
        return redirect("admins:admin-home")
    
    # if user is Manager it will be redirectto manager-home page that is located in manager app
    elif request.user.role == "manager":
        return redirect("manager:manager-home")
    
    # if user is Employee it will be redirectto employee-home page that is located in manager app
    elif request.user.role == "employee":
        return redirect("employee:employee-home")

    return render(request, "main/home.html")



@login_required(login_url="account:login")
def my_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "main/notification.html",locals())


def login_view(request):  
    if request.POST:
        getEmail = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=getEmail, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status':"success"})
        else:
            return JsonResponse({'status':"Credentails are not matched"})
    return render(request , "account/login.html")


def logout_view(request):
    logout(request)
    return redirect('account:login')

