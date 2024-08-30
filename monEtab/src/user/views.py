from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm
#from .models import User


# Create your views here.
@login_required
def list(request):

    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request,'listUser.html', context)


@login_required
def add(request):

    if request.method == "POST":
        print(request.POST)
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_form.save()
            return redirect('user:list')
        else:
            return render(request, 'user:modifierUser.html', context)

    user_form = UserForm()
    
    context = {'user_form': user_form }
    return render(request, 'addUser.html', context)


@login_required
def update(request,id):

    user = User.objects.get(id = id)

    context = {
        'title': 'modification utilisateur'
    }

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance = user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list')
    
    # user = User.objects.get(id = id)

    user_form = UserForm(instance = user)

    context["user_form"] = user_form

    return render(request, 'updateUser.html', context)


@login_required
def delete(request, id):

    user = User.objects.get(id = id)
    user.delete()

    return redirect('user:list')