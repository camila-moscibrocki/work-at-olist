from books.models import Book
from authors.models import Author
from rest_framework.serializers import ModelSerializer
from authors.api.serializers import AuthorSerializer


class BookSerializer(ModelSerializer):
    """
    Create a serializer for book's class using ModelSerializer and indicates the relationship between author's serializer (nested)
    """
    author = AuthorSerializer(many=True)

    class Meta:
        """
        Indicates model
        """
        model = Book
        """
        Indicates fields for application
        """
        fields = ['id', 'title', 'edition', 'publication_year', 'author']

