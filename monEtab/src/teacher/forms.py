from django import forms

class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=10)
    last_name = forms.CharField(max_length=30)
    birth_date = forms.DateField()
    city = forms.CharField(max_length=30)
    number = forms.CharField(max_length=10)
    vacation = forms.BooleanField()
    subject_taught = forms.CharField(max_length=30)
    next_course = forms.CharField(max_length=30)
    subject_next_meet = forms.CharField(max_length=30)