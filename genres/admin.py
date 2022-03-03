from django.contrib import admin
from genres.models import Genre

class Genres(admin.ModelAdmin):
    link_display = ('name',)
    search_fields = ('name',)

admin.site.register(Genre,Genres)
