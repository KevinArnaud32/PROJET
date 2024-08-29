from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
def list(request):

    teachers = Teacher.objects.all();

    context = {
        'teachers': teachers
    }

    return render(request,'listTeacher.html', context)

def add(request):

    if request.method == 'POST':
        #print(request.POST)
        teacher_form = TeacherForm(request.POST)

        if teacher_form.is_valid():
            print(teacher_form.cleaned_data)
            teacher_form.save()
            return redirect('teacher:list')

    teacher_form = TeacherForm()

    form = TeacherForm()
    context = {'teacher_form': teacher_form }
    return render(request, 'addTeacher.html', context)

def modifierTeacher(request, id):

    teacher = Teacher.objects.get(id = id)

    context = {
        'title': 'Modification Professeur'
    }

    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST, instance= teacher)
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect('teacher:list')
        
    teacher_form = TeacherForm(instance=teacher)

    context['teacher_form'] = teacher_form

    return render(request, 'updateTeacher.html', context)

def supprimerTeacher(request, id):

    teacher = Teacher.objects.get(id = id)
    teacher.delete()

    return redirect('teacher:list')