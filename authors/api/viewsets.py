from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from authors.models import Author
from authors.api.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    """
    Create the view set for author using ModelsViewSet
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    """
    Create tools for search and filters using Django_Filters.
    """
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'name')
    filter_fields = ('id', 'name')
