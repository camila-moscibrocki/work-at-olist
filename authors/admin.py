from django.contrib import admin
from .models import Author

"""
Include "Author" Model in Admin
"""
admin.site.register(Author)
