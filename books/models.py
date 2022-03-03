from django.db import models
from genres.models import Genre
from authors.models import Author

class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    artist = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
