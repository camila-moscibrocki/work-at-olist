from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from books.models import Book
from books.api.serializers import BookSerializer, BookListSerializer


class BookViewSet(ModelViewSet):
    """
    Create the view set for books using ModelsViewSet
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """
    Create tools for search and filters using Django_Filters.
    """
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'title', 'publication_year')
    filter_fields = ('title', 'edition', 'publication_year', 'author')
    lookup_field = 'title'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookListSerializer
        return BookSerializer