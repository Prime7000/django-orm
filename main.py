import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from myapp.models import Book

# Create an entry
Book.objects.create(title="how to love", author="senu")

# Fetch all books
for book in Book.objects.all():
    print(book)
