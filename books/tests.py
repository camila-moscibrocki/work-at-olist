from rest_framework.test import APITestCase
from authors.models import Author


"""
This test send a new book in json format using method POST
"""
class BooksAPITestCase(APITestCase):
    def test_post_book(self):
        Author.objects.create(name="Luiz Henrique Hugria")
        response = self.client.post('/books/', {'title': 'Introduction to finite element analysis', 'edition': 3, 'publication_year': 1990, 'authors': [1]}, format='json')
        self.assertEqual(response.status_code, 201)
