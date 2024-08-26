from django import forms
from .models import User

class MyForm(forms.Form):
    pseudo_name = forms.CharField(max_length=30)
    password = forms.CharField(min_length=8, max_length=12, widget=forms.PasswordInput())
    creat_at = forms.DateField()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo_name', 'pass_word']
        #exclude = ("creat_at")