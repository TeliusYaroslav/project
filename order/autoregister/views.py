from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
# Create your views here.


def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password == password_confirm:
            try:
                User.objects.create_user( username=username, password=password )
                return redirect('login')
            except IntegrityError:
                return render(request, 'autoregister/register.html', context = {'user_error':'This user exsist'})
        else:
            return render(request, 'autoregister/register.html', context = {'user_error':'Passwords aren`t the same'})      
    # return render(request, 'mainpage/main.html')
    return render(request, 'autoregister/register.html')






def success_register(request):
    return render(request, 'mainpage/main.html')

def view_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'autoregister/index.html', context={'log_error': 'password or login isn`t correct'})
    return render(request, 'autoregister/index.html')

# def login1(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('MainPage1')
#         else:
#             return render(request, "login/login.html", context = {"log_error": "Користувача не знайдено"})

#     return render(request, "login/login.html")
        
def show_succesful_login(request):
    if request.user.is_authenticated:
        return render(request, 'mainpage/main.html')
    
def logout2(request):
    logout(request)
    return redirect("main")    

