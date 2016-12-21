from django.db import models

# Create your models here.
"""when making a newsletter what kind of forms do the user fill out to get the newsletter when its available

name, email fields

models maps these fields and stores into a db
"""

class SignUp(models.Model):
	full_name = models.CharField(max_length=120, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.email