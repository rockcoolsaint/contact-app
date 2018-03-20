from django.forms import ModelForm, CharField, EmailField, TextInput
from django import forms
from .models import Contact

class ContactForm(ModelForm):
	name= CharField(widget=TextInput(
		attrs={
			'class': 'form-control',
		}
	))

	email = EmailField(widget=TextInput(
		attrs={
			'class': 'form-control',
		}
	))

	class Meta:
		model = Contact
		fields = ['name', 'email']
		widgets = {
			'name': TextInput(attrs={
				'class': 'form-control',
			}),
			'email': TextInput(attrs={
				'class': 'form-control',
			})
		}
