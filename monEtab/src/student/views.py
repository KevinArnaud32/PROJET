from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def list(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'listStudent.html', context)


def add(request):
    
    if request.method == 'POST':
        #print(request.POST)
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            print(student_form.cleaned_data)
            student_form.save()
            return redirect('student:list')

    student_form = StudentForm()
    form = StudentForm()

    context = {'student_form': student_form }
    return render(request, 'addStudent.html', context)


def update(request, id):
    
    student = Student.objects.get(id = id)

    context = {
        'title': 'modification student'
    }

    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance = student)
        if student_form.is_valid():
            student_form.save()
            return redirect('student:list')
    
    student_form = StudentForm(instance = student)

    context["student_form"] = student_form

    return render(request, 'updateStudent.html', context)


def supprimerStudent(request, id):

    student = Student.objects.get(id = id)
    student.delete()

    return redirect('student:list')