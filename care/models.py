from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class Upload(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    phone=PhoneNumberField()
    whatsappphone=PhoneNumberField()
    street=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    zip=models.CharField( max_length=6)
    age=models.CharField( max_length=50,)
    gender=models.CharField( max_length=50)
    workclass=models.CharField( max_length=50)
    education=models.CharField( max_length=50)
    maritalstatus=models.CharField( max_length=50)
    hoursofwork=models.CharField( max_length=50)
    income=models.CharField( max_length=50)
    filepath = models.ImageField(upload_to = "media/images", null = True, blank=True)
    tdr=models.CharField( max_length=50)
    class Meta:
        db_table:"info"

class DonorProfile(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=50)
    phone=PhoneNumberField()
    whatsappphone=PhoneNumberField()
    street=models.CharField( max_length=50)
    city=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    zip=models.CharField( max_length=6)
    idi=models.CharField( max_length=50)
    class Meta:
        db_table:"donorprofile"


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

		labels={ 
			'username' : _('Username'),
			'email' : _('Email'),
			'password1' : _('Password'),
			'password2' : _('Confirm Password')
			}

widgets = {
		'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id':'inputusername'}),
		'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email','id':'inputEmail'}),
		'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password','id':'inputPassword'}),
		'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password','id':'inputPassword'}),
		}