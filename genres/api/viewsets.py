from rest_framework import viewsets
from genres.models import Genre
from genres.api.serializer import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer