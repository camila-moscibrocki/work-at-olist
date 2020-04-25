from authors.models import Author
from rest_framework.serializers import ModelSerializer


class AuthorSerializer(ModelSerializer):
    """
    Create a serializer for author's class using ModelSerializer
    """
    class Meta:
        """
        Indicates model
        """
        model = Author
        """
        Indicates fields for application
        """
        fields = ['id', 'name']
