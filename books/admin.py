from django.contrib import admin
from books.models import Book

class Books(admin.ModelAdmin):
    link_display = ('name','genre','artist')
    search_fields = ('name','genre','artist')

admin.site.register(Book,Books)
