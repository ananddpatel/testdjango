from django import forms
# from django.forms import widgets
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		# only allows use of mail.utoronto.ca emails
		# can be used to validate any other fields with clean_<field_name>

		email = self.cleaned_data.get('email')
		email_base, domain = email.split('@')
		if domain != 'mail.utoronto.ca':
			raise forms.ValidationError('Please use a valid your UofT email')
		return email

class EERForm(forms.Form):
	height = forms.IntegerField()
	weight = forms.IntegerField()
	age = forms.IntegerField()
	sex_choices = (
		('Male', 'MALE'),
		('Female', 'FEMALE'),
		)
		# inner tuple ('data thats get sent via POST', 'whats shown on form')
	sex_field = forms.ChoiceField(choices=sex_choices)

	def clean_weight(self):
		# only allows use of mail.utoronto.ca emails
		# can be used to validate any other fields with clean_<field_name>
		weight = self.cleaned_data.get('weight')
		if weight <= 0:
			raise forms.ValidationError('Please use a valid weight in Kg')
		return weight

	def clean_age(self):
		# only allows use of mail.utoronto.ca emails
		# can be used to validate any other fields with clean_<field_name>
		age = self.cleaned_data.get('age')
		if age <= 0:
			raise forms.ValidationError('Please use a valid age in Years')
		return age

	def clean_height(self):
		# only allows use of mail.utoronto.ca emails
		# can be used to validate any other fields with clean_<field_name>
		height = self.cleaned_data.get('height')
		if height <= 0:
			raise forms.ValidationError('Please use a valid height in cm')
		return height

class ContactForm(forms.Form):
	name = forms.CharField(max_length=120)
	subject = forms.CharField(max_length=150)
	email = forms.EmailField()
	message = forms.CharField(max_length=11500, widget=forms.Textarea)

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == '':
			raise forms.ValidationError('Please enter your name.')
		return name

	def clean_subject(self):
		subject = self.cleaned_data.get('subject')
		if subject == '':
			raise forms.ValidationError('Please enter a Subject heading.')
		return subject