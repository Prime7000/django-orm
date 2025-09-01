from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	age = models.CharField(max_length=10, null=True)

	class Meta:
		app_label = "myapp"

	def __str__(self):
		return f"{self.title} by {self.author}"


'''
Note you must use 
	python manage.py makemigrations myapp
to make migrations
'''
