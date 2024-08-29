from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','birth_date','city','number','vacation','subject_taught','next_course','subject_next_meet']
        