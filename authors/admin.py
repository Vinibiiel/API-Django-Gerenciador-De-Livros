from django.contrib import admin
from authors.models import Author

class Authors(admin.ModelAdmin):
    link_display = ('name',)
    search_fields = ('name',)

admin.site.register(Author,Authors)
