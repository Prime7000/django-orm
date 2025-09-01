import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from myapp.models import Book

# Create an entry
Book.objects.create(title="Django ORM", author="Prime")

# Fetch all books
for book in Book.objects.all():
    print(book)
