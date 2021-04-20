from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from NoteApp.models import ComplaintBox,ImProfile



class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"UserName",
			}),

		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=ComplaintBox
		fields="__all__"
class ImForm(forms.ModelForm):
	class Meta:
		model=ImProfile
		fields=['age','gender',"impf"]
		widgets={
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age",}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select your gender",}),
		}

class UtupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control"}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"updateemail",}),
		}

class ChPwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"enter old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"enter new password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(
		attrs={'class':"form-control", 'placeholder':"Confirm new password"}))
	class Meta:
		model=User
		fields='__all__'
