from django.contrib import admin

# Register your models here.
from .models import book_store

admin.site.register(book_store)
