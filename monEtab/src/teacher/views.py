from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TeacherForm
from .models import Teacher

# Create your views here.
@login_required
def list(request):

    teachers = Teacher.objects.all();

    context = {
        'teachers': teachers
    }

    return render(request,'listTeacher.html', context)

@login_required
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

@login_required
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

@login_required
def supprimerTeacher(request, id):

    teacher = Teacher.objects.get(id = id)
    teacher.delete()

    return redirect('teacher:list')