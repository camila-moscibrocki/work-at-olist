from django.core.management import call_command
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Author
from books.models import Book

import os


class AuthorTest(TestCase):

    """
    This test creates a CSV file using the custom command "import" from management>command directory
    """

    def test_import(self):
        content = 'name\n'
        authors = ['Mauricio Samy Silva', 'Pablo Dall Oglio', 'Yehuda Katz']
        content += '\n'.join(iter(authors))
        filename = 'authors_list.csv'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        call_command('import', filename)
        os.remove(filename)
        authors = Author.objects.all()
        self.assertEqual(authors.count(), len(authors))


    def test_create(self):
        author = Author.objects.create(name='Bibeault')
        self.assertEqual(author.name, 'Bibeault')
        authors = Author.objects.all()
        count = authors.count()
        self.assertEqual(count, 1)

    """
    This test send a new author in json format using method POST
    """

class Authors(APITestCase):
    def test_post_author(self):
        response = self.client.post('/authors/', {'name': 'Carl Sagan'}, format='json')
        self.assertEqual(response.status_code, 201)
