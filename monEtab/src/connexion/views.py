from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
 


# Create your views here.
def sign_in(request):
    
    # next_url = request.GET.get('next','')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.GET.get('next')

        user = authenticate(request, username = username, password = password)


        if user is not None:
            # print(next_url)

            login(request, user)
            if next:
                return redirect(next)
            return redirect('dashboard:index')
            
            #return redirect('user:list')
        else:
            messages.error(request, "Nom utilisateur ou mot de passe incorect.")

    return render(request, 'login.html')


def sign_up(request):

    if request.method == 'POST':
        username = request.POST.get('pseudo','')
        password = request.POST.get('pwd','')
        if not username or not password:
            return render(request,'register.html')
        
        user = User(username = username)
        user.save() 

        user.password = password
        user.set_password(user.password)
        user.save()
        login(request,user)
        return redirect('user:list')

    return render(request, 'register.html')


def log_out(request):

    logout(request)

    return redirect('connexion:sign_in')