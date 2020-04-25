from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['id']
        indexes = [
            models.Index(fields=['name'], name='idx_author_name')
        ]