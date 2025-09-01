from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)

	class Meta:
		app_label = "myapp"

	def __str__(self):
		return f"{self.title} by {self.author}"



