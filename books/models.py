from django.db import models
from authors.models import Author


class Book(models.Model):

    title = models.CharField(max_length=150)
    edition = models.FloatField()
    publication_year = models.IntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']
        indexes = [
            models.Index(fields=['title'], name='idx_book_title'),
            models.Index(fields=['publication_year'], name='idx_book_publication_year')
            ]