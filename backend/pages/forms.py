from django import forms
from django.utils.translation import gettext as _


class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"placeholder": _('Имя')}))
	email = forms.EmailField(max_length = 150, widget=forms.TextInput(attrs={"placeholder": _('Email')}))
	subject = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={"placeholder": _('Название')}))
	message = forms.CharField(max_length = 2000, widget=forms.Textarea(attrs={"placeholder": _('Сообщение')}))