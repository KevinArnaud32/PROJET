from django.http import HttpResponse
from django.shortcuts import render
from .forms import TeacherForm

# Create your views here.
def index(request):
    return render(request,'teacher/index.html')

def ajouterTeacher(request):
    form = TeacherForm()
    context = { 'form': form }
    return render(request, 'teacher/ajouterTeacher.html', context)

def modifierTeacher(request):
    form = TeacherForm()
    context = { 'form': form }
    return render(request, 'teacher/modifierTeacher.html', context)