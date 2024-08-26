from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length = 10)
    last_name = forms.CharField(max_length = 10)
    birth_date = forms.DateField()
    city = forms.CharField(max_length=30)
    number = forms.CharField(max_length=10)
    class_student = forms.CharField(max_length=30)
    register_number = forms.CharField(max_length=30)