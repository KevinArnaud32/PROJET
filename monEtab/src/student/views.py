from django.http import HttpResponse
from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'student/index.html')

def ajoutStudent(request):
    form = StudentForm()
    context = { 'form': form }
    return render(request, 'student/ajouterstudent.html', context)

def updateStudent(request):
    form = StudentForm()
    context = { 'form': form }
    return render(request, 'student/updateStudent.html', context)