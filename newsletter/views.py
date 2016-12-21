from django.conf import settings
from django.shortcuts import render
from .forms import SignUpForm, EERForm, ContactForm
from .calculations import calculate_eer
from django.core.mail import send_mail
from .models import SignUp

# Create your views here.

def home(request):
	context = {}
	if request.user.is_authenticated() and request.user.is_staff:
		queryset = SignUp.objects.all()
		context = {
			'queryset': queryset
		}

	return render(request, 'home.html', context)

def signup(request):
	# if request.user.is_authenticated():
	# 	my_title = 'Hello {0}!'.format(request.user)
	# else:
	# 	my_title = 'Welcome!'
	# print(request.POST)
	my_form = SignUpForm(request.POST or None)

	if my_form.is_valid():
		my_form.save()

	context = {
		'my_title': 'Sign-Up',
		'form': my_form
	}
	return render(request, 'signup.html', context)

def EER(request):
	data = request.POST
	eer_form = EERForm(data or None)

	if eer_form.is_valid():
		eer = calculate_eer(
			data.get('sex_field'), 
			data.get('age'), 
			data.get('weight'), 
			data.get('height')
			)
		display = 'Your EER is: {}'.format(eer)
	else:
		display = ''

	context = {
		'title': 'Calculate EER',
		'form': eer_form,
		'eer_display': display
	}

	return render(request, 'eer.html', context)

def contact(request):
	data = request.POST
	form = ContactForm(data or None)

	name = data.get('name')
	subject = data.get('subject')
	email = data.get('email')
	message = data.get('message')

	if form.is_valid():
		send_mail(
		    subject,
		    'From: {0}\nContact E-Mail: {1}\n\n {2}'.format(name, email, message),
		    settings.EMAIL_HOST_USER,
		    [settings.EMAIL_HOST_USER],
		    fail_silently=False,
		)
	context = {
		'form': form,
	}
	return render(request, 'contact.html', context)