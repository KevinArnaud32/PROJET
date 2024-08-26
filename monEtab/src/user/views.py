from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm, UserForm

# Create your views here.
def index(request):
    return render(request,'user/index.html')

def ajouterUser(request):

    if request.method == "post":
        print(request.POST)
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            print(user_form.cleaned_data)

    user_form = UserForm()
    my_form = MyForm()
    
    context = { 'my_form': my_form, 'user_form': user_form }
    return render(request, 'user/ajouterUser.html', context)

def modifierUser(request):
    my_form = MyForm()
    context = { 'my_form': my_form }
    return render(request, 'user/update.html', context)