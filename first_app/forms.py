from django import forms
from first_app.models import student

class student_form(forms.ModelForm):
	class Meta():
		model=student
		fields="__all__"