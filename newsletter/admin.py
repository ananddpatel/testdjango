from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['email', 'full_name', 'timestamp']
	search_fields = ['email', 'full_name',]

	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)