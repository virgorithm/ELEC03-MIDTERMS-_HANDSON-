from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Account, Subjects, Personal_Information, Programs, Teachers


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
        field.widget.attrs.update({
            'class': 'form-control',
            'placeholder': field.label
        })

class AccountForm (forms.ModelForm):
    class Meta:
        model = Account 
        fields ='__all__'

# class SubjectsForm (forms.ModelForm):
#     class Meta:
#         model = Subjects 
#         fields ='__all__'



class CustomRegisterForm(UserCreationForm):
    student_Id = forms.CharField(max_length=100)
    lrn = forms.IntegerField()
    gender = forms.ChoiceField(choices=Personal_Information.gender_choices)
    phone_number = forms.IntegerField()
    address = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'student_Id', 'lrn', 'gender', 'phone_number', 'address']

# class ProgramsForm (forms.ModelForm):
#     class Meta:
#         model = Programs 
#         fields ='__all__'

# class TeachersForm (forms.ModelForm):
#     class Meta:
#         model = Teachers 
#         fields ='__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text = 'Required. Enter a valid email address' )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control custom-input',
        'placeholder': 'Enter username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control custom-input',
        'placeholder': 'Enter password'
    }))